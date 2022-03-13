import requests as r
from classes.config import API_KEY


class Movie:
    def __init__(self, id):
        self._id = id

        api_url = f"https://api.themoviedb.org/3/movie/{self.id}?api_key={API_KEY}&language=fr"

        response = r.get(api_url).json()
        # print(json.dumps(response, sort_keys=True, indent=4))

        self._title = response['title']
        self._description = response['overview']
        self._img = 'https://image.tmdb.org/t/p/w500' + response['poster_path']
        self._date = response['release_date']

# Getters
    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title
    
    @property
    def description(self):
        return self._description

    @property
    def img(self):
        return self._img

    @property
    def date(self):
        return self._date


    def context(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "img": self.img,
            "date": self.date,
        }