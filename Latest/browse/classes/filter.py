import requests as r
from .config import API_KEY
from .movies import Movie
from .series import Serie
from browse.models import Movie as Movie_DB
from browse.models import Serie as Serie_DB


def movie_popular() -> list :
    """ Va chercher dans l'API TMDB les Films les plus populaires du moment.
    In : rien
    Out : movies : liste d'instances de la classe Movie
    """
    api_url = f"http://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    movies = []
    for result in response['results']:
        movies.append(Movie(result['id']))

    return movies


def movie_upcoming() -> list :
    """ Va chercher dans l'API TMDB les Films qui vont sortir prochainement.
    In : rien
    Out : movies : liste d'instances de la classe Movie
    """
    api_url = f"http://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=fr&region=FR"
    response = r.get(api_url).json()

    movies = []
    for result in response['results']:
        movies.append(Movie(result['id']))

    return movies


def serie_popular() -> list :
    """ Va chercher dans l'API TMDB les Séries les plus populaires du moment.
    In : rien
    Out : series : liste d'instances de la classe Serie
    """
    api_url = f"http://api.themoviedb.org/3/tv/popular?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    series = []
    for result in response['results']:
        series.append(Serie(result['id']))

    return series


def latest_movie() -> object :
    """ Va chercher dans l'API TMDB le dernier film publié.
    In : rien
    Out : instance de la classe Movie
    """
    api_url = f"http://api.themoviedb.org/3/movie/latest?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    return Movie(response['id'])


def latest_serie() -> object :
    """ Va chercher dans l'API TMDB la dernière série publiée.
    In : rien
    Out : instance de la classe Serie
    """
    api_url = f"http://api.themoviedb.org/3/tv/latest?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    return Serie(response['id'])


def total_popular() -> dict :
    """ Retourne les films et les séries les plus populaires du moment.
    In : rien
    Out : dictionnaire contennant 2 listes d'instances des classes Movie et Serie
    """
    return {
        'movies': movie_popular(),
        'series': serie_popular(),
    }


def upcoming():
    """ Retourne tous les films et toute les séries qui viennet de sortir ou qui ne sont pas encore sortis.
    In : rien
    Out : dictionnaire contennant 3 listes d'instances des classes Movie et Serie
    """
    return {
        'upcoming_movies': movie_upcoming(),
        'latest_movie': latest_movie(),
        'latest_serie': latest_serie(),
    }


def movie_in_db(status) -> object :
    """ Va chercher les films présents dans la base de données.
    In : rien
    Out : movies : liste d'instances de la classe Movie
    """
    movies = []
    for movie in Movie_DB.objects.filter(status=status).order_by('-date'):
        movies.append(Movie(movie.id))

    return movies


def serie_in_db(status) -> object :
    """ Va chercher les séries présentes dans la base de données.
    In : rien
    Out :  series : liste d'instances de la classe Serie
    """
    series = []
    for serie in Serie_DB.objects.filter(status=status).order_by('-date'):
        series.append(Serie(serie.id))

    return series
    

def total_in_db(status) -> dict :
    """ Retourne les films et les séries présents dans la base de données.
    In : rien
    Out : dictionnaire contennant 2 listes d'instances des classes Movie et Serie
    """
    get_total_dir()
    return {
        'movies': movie_in_db(status),
        'series': serie_in_db(status),
    }


def search_movie(query:str) -> (list, int) :
    """ Va chercher dans l'API TMDB tous les films correspondants à la recherche.
    In : query (str) : recherche
    Out : movies : liste d'instances de la classe Movie
          max_popularity (int) : popularité du 1er résultat pour afficher le meilleur en 1er
    """
    api_url = f"http://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=fr&query={query}"
    api_response = r.get(api_url).json()

    max_popularity = api_response['results'][0]['popularity'] if api_response['results'] != [] else 0

    movies = []
    for result in api_response['results']:
        movies.append(Movie(result['id']))

    return movies, max_popularity


def search_serie(query:str) -> (list, int) :
    """ Va chercher dans l'API TMDB toutes les séries correspondantes à la recherche.
    In : query (str) : recherche
    Out : series : liste d'instances de la classe Serie
          max_popularity (int) : popularité du 1er résultat pour afficher le meilleur en 1er
    """
    api_url = f"http://api.themoviedb.org/3/search/tv?api_key={API_KEY}&language=fr&query={query}"
    api_response = r.get(api_url).json()
    max_popularity = api_response['results'][0]['popularity'] if api_response['results'] != [] else 0

    series = []
    for result in api_response['results']:
        series.append(Serie(result['id']))

    return series, max_popularity


def search_query(query:str) -> dict :
    """ Retourne les films et les séries correspondants à la recherche.
    In : query (str) : recherche
    Out : dictionnaire contennant 2 listes d'instances des classes Movie et Serie
    """
    if query != None:
        movies = search_movie(query)
        series = search_serie(query)
        most_popular = 'Films' if movies[1] >= series[1] else 'Séries' # Détermine le 1er résultat à afficher
        return {
                'query': query,
                'most_popular': most_popular,
                'movies': movies[0],
                'series': series[0],
            }


def get_movie_video(id:int) -> str :
    """ Retourne la clé YouTube de la prmière vidéo trouvée dans l'API
    In : id (int) : id du film
    Out : key (str) : clé YouTube
    """
    api_url = f"http://api.themoviedb.org/3/movie/{id}/videos?api_key={API_KEY}&language=fr"
    api_response = r.get(api_url).json()

    key = ''
    for result in api_response['results']:
        if result['site'] == 'YouTube':
            key = result['key']

    return key


def get_episode_video(id:int, season_num:int, episode_num:int) -> str :
    """ Retourne la clé YouTube de la prmière vidéo trouvée dans l'API
    In : id (int) : id du film
         season_num (int) : numéro de la saison
         episode_num (int) : numéro de l'épisode
    Out : key (str) : clé YouTube
    """
    # Cherche une vidéo sur l'épisode
    api_url = f"http://api.themoviedb.org/3/tv/{id}/season/{season_num}/episode/{episode_num}/videos?api_key={API_KEY}&language=fr"
    api_response = r.get(api_url).json()

    # Si aucune vidéo trouvée sur l'épisode alors cherche sur la saison entière
    if api_response['results'] == []:
        api_url = f"http://api.themoviedb.org/3/tv/{id}/season/{season_num}/videos?api_key={API_KEY}&language=fr"
        api_response = r.get(api_url).json()

    # Si aucune vidéo trouvée sur la saison alors cherche sur la série entière
    if api_response['results'] == []:
        api_url = f"http://api.themoviedb.org/3/tv/{id}/videos?api_key={API_KEY}&language=fr"
        api_response = r.get(api_url).json()

    key = ''
    for result in api_response['results']:
        if result['site'] == 'YouTube':
            key = result['key']
            break

    return key


def get_watch_list():
    movies_db = Movie_DB.objects.filter(status='listed')
    movies = [Movie(movie.id) for movie in movies_db]

    series_db = Serie_DB.objects.filter(status='listed')
    series = [Serie(serie.id) for serie in series_db]

    return {
        'movies': movies,
        'series': series,
    }


def add_to_list(genre, id):
    if genre == 'movie':
        movie = Movie(id)
        movie.to_db('listed')
        return movie.context()
    else:
        serie = Serie(id)
        serie.to_db('listed')
        return serie.context()


def remove_from_list(genre, id):
    if genre == 'movie':
        movie = Movie(id)
        movie.to_db('clicked')
        return movie.context()
    else:
        serie = Serie(id)
        serie.to_db('clicked')
        return serie.context()

    
