from curses.ascii import HT
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from .classes.movies import Movie
from .classes.series import Serie, Season, Episode
import browse.classes.filter as filter


def index(request):
    return render(request, "index.html", context=filter.total_in_db())


def watchlist(request):
    return render(request, "watchlist.html", context=filter.get_watch_list())

def add_to_watchlist(request, genre, id):
    return render(request, "watchlist.html", context=filter.add_to_list(genre, id))


def popular(request):
    return render(request, "index.html", context=filter.total_popular())


def latest(request):
    return render(request, "latest.html", context=filter.upcoming()) 


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

    return render(request, "search.html", context=filter.search_query(query))


def watch_movie(request, id):
    return render(request, "watch.html", context={ 'key': get_movie_video(id) })


def watch_serie(request, id, season_num, episode_num):
    return render(request, "watch.html", context={ 'key': get_episode_video(id, season_num, episode_num) })