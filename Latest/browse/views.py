from django.shortcuts import render
from markupsafe import re
from .classes.movies import Movie
from .classes.series import Serie, Season, Episode
from .classes.filter import total_popular, upcoming, search_query, total_in_db


def index(request):
    return render(request, "index.html", context=total_in_db())


def watchlist(request):
    return render(request, "watchlist.html", context=None)


def popular(request):
    return render(request, "index.html", context=total_popular())


def latest(request):
    return render(request, "latest.html", context=upcoming()) 


def movie(request, id):
    return render(request, "movie.html", context=Movie(id).context())


def serie(request, id):
    return render(request, "serie.html", context=Serie(id).context())


def season(request, serie_id, season_num):
    return render(request, "season.html", context=Season(serie_id, season_num).context())
    

def search(request, query):
    return render(request, "search.html", context=search_query(query))