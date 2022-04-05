import os
from .movies import Movie
from .series import Serie
from browse.models import Movie as Movie_DB
from browse.models import Serie as Serie_DB


def get_movies_dir():
    movies = []
    moviesdir = os.listdir('browse/static/films')
    for moviedir in moviesdir:
        id = int(moviedir.split('.')[0])
        movie = Movie(id)
        movie.to_db('owned')
        movies.append(movie)
    return movies


def get_series_dir():
    series = []
    seriesdir = os.listdir('browse/static/series')
    for seriedir in seriesdir:
        id = int(seriedir.split('.')[0])
        serie = Serie(id)
        serie.to_db('owned')
        series.append(serie)
    return series 


def get_total_dir():
    movies_db = Movie_DB.objects.filter(status='owned')
    movies_id = [movie.id for movie in movies_db]
    movies_dir = [movie.id for movie in get_movies_dir()]

    for movie in movies_id:
        if movie not in movies_dir:
            Movie(movie).to_db('clicked')
        

    series_db = Serie_DB.objects.filter(status='owned')
    series_id = [serie.id for serie in series_db]