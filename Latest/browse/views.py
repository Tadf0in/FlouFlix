from django.shortcuts import render
from classes.movies import Movie
from classes.series import Serie, Season, Episode



def movie(request, id):
    return render(request, "movie.html", context=Movie(id).context())


def serie(request, id):
    return render(request, "serie.html", context=Serie(id).context())

def season(request, serie_id, season_num):
    return render(request, "season.html", context=Season(serie_id, season_num).context())
