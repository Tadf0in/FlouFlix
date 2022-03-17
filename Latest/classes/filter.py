import imp
import requests as r
from classes.config import API_KEY
from classes.movies import Movie
from classes.series import Serie


def movie_filter(filtre):
    api_url = f"http://api.themoviedb.org/3/movie/{filtre}?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    movies = []
    for result in response['results']:
        movies.append(Movie(result['id']))

    return movies


def serie_filter(filtre):
    api_url = f"http://api.themoviedb.org/3/tv/{filtre}?api_key={API_KEY}&language=fr"
    response = r.get(api_url).json()

    movies = []
    for result in response['results']:
        movies.append(Serie(result['id']))

    return movies


def total_filter(filtre):
    return {
        'filter': filtre,
        'movies': movie_filter(filtre),
        'series': serie_filter(filtre),
    }