from django.shortcuts import render
from django.http import HttpResponse

API_KEY = ""


class Movie:
    def __init__(self, id):
        self.id = id
        self.api_url = f"https://api.themoviedb.org/3/movie/{self.id}?api_key={API_KEY}&language=fr"

    
    def request_api(self):
        pass


movietest = Movie(0)


def index(request):
    return HttpResponse(movietest.api_url)


