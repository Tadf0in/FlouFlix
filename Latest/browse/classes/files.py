import os
from .movies import Movie
from .series import Serie
from browse.models import Movie as Movie_DB
from browse.models import Serie as Serie_DB


def get_movies_dir():
    moviesdir = os.listdir('browse/static/films')
    for moviedir in moviesdir:
        id = int(moviedir.split('.')[0])
        movie = Movie(id)
        movie.to_db('owned')


def get_series_dir():
    seriesdir = os.listdir('browse/static/series')
    for seriedir in seriesdir:
        id = int(seriedir.split('.')[0])
        serie = Serie(id)
        serie.to_db('owned')


def get_total_dir():
    get_movies_dir()
    get_series_dir()