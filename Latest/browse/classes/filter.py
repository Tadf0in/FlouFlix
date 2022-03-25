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


def movie_in_db() -> object :
    """ Va chercher les films présents dans la base de données.
    In : rien
    Out : movies : liste d'instances de la classe Movie
    """
    movies = []
    for movie in Movie_DB.objects.all():
        movies.append(Movie(movie.id))

    return movies


def serie_in_db() -> object :
    """ Va chercher les séries présentes dans la base de données.
    In : rien
    Out :  series : liste d'instances de la classe Serie
    """
    series = []
    for serie in Serie_DB.objects.all():
        series.append(Serie(serie.id))

    return series
    


def total_in_db() -> dict :
    """ Retourne les films et les séries présents dans la base de données.
    In : rien
    Out : dictionnaire contennant 2 listes d'instances des classes Movie et Serie
    """
    return {
        'movies': movie_in_db(),
        'series': serie_in_db(),
    }



def search_movie(query):
    """ Va chercher dans l'API TMDB tous les films correspondants à la recherche.
    In : query (str) : recherche
    Out : movies : liste d'instances de la classe Movie
    """
    api_url = f"http://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=fr&query={query}"
    api_response = r.get(api_url).json()

    movies = []
    for result in api_response['results']:
        movies.append(Movie(result['id']))

    return movies


def search_serie(query):
    """ Va chercher dans l'API TMDB toutes les séries correspondantes à la recherche.
    In : query (str) : recherche
    Out : series : liste d'instances de la classe Serie
    """
    api_url = f"http://api.themoviedb.org/3/search/tv?api_key={API_KEY}&language=fr&query={query}"
    api_response = r.get(api_url).json()

    series = []
    for result in api_response['results']:
        series.append(Serie(result['id']))

    return series


def search_query(query):
    """ Retourne les films et les séries correspondants à la recherche.
    In : query (str) : recherche
    Out : dictionnaire contennant 2 listes d'instances des classes Movie et Serie
    """
    if query != None:
        return {
            'movies': search_movie(query),
            'series': search_serie(query),
        }