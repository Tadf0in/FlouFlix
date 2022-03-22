import requests as r
from .config import API_KEY
from .movies import Movie
from .series import Serie


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

    movies = []
    for result in response['results']:
        movies.append(Serie(result['id']))

    return movies


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


def search_query(query):
    """
    """
    api_url = f"http://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=fr&query={query}"
    response = r.get(api_url).json()

    