from django.shortcuts import render
from markupsafe import re
from classes.movies import Movie
from classes.series import Serie, Season, Episode
from classes.filter import total_filter


def index(request):
    return render(request, "index.html", context={'filter': None})


def filter(request, filter):
    return render(request, "index.html", context=total_filter(filter))


def movie(request, id):
    return render(request, "movie.html", context=Movie(id).context())


def serie(request, id):
    return render(request, "serie.html", context=Serie(id).context())


def season(request, serie_id, season_num):
    return render(request, "season.html", context=Season(serie_id, season_num).context())
