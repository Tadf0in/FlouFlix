from django.shortcuts import render
from classes.movies import Movie


def movie(request, id):
    return render(request, "index.html", context=Movie(id).context())
