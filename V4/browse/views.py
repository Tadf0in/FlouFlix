from curses.ascii import HT
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from .classes.movies import Movie
from .classes.series import Serie, Season, Episode
from .classes.filter import total_popular, upcoming, search_query, total_in_db, get_movie_video, get_episode_video


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
    

def search(request):
    try:
        query = request.GET['q'] 
    except MultiValueDictKeyError:
        query = None

    return render(request, "search.html", context=search_query(query))


def watch_movie(request, id):
    return render(request, "watch.html", context={ 'key': get_movie_video(id) })


def watch_serie(request, id, season_num, episode_num):
    return render(request, "watch.html", context={ 'key': get_episode_video(id, season_num, episode_num) })