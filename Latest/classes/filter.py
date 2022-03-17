import requests as r
from classes.config import API_KEY
from classes.movies import Movie
from classes.series import Serie


def movie_popular():
    api_url = f"http://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    movies = []
    for result in response['results']:
        movies.append(Movie(result['id']))

    return movies


def movie_upcoming():
    api_url = f"http://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=fr&region=FR"
    response = r.get(api_url).json()

    movies = []
    for result in response['results']:
        movies.append(Movie(result['id']))

    return movies


def serie_popular():
    api_url = f"http://api.themoviedb.org/3/tv/popular?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    movies = []
    for result in response['results']:
        movies.append(Serie(result['id']))

    return movies


def latest_movie():
    api_url = f"http://api.themoviedb.org/3/movie/latest?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    return Movie(response['id'])


def latest_serie():
    api_url = f"http://api.themoviedb.org/3/tv/latest?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    return Serie(response['id'])


def total_popular():
    return {
        'movies': movie_popular(),
        'series': serie_popular(),
    }


def upcoming():
    return {
        'upcoming_movies': movie_upcoming(),
        'latest_movie': latest_movie(),
        'latest_serie': latest_serie(),
    }


def search_query(query):
    api_url = f"http://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=fr&query={query}"
    response = r.get(api_url).json()

    