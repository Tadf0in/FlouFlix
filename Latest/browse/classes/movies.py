import requests as r
from .config import API_KEY
from browse.models import Movie as DB_Movie


class Movie:
    """
    Passe les informations d'un film récupérées dans l'API TMDB sous forme de classe.
    """
    def __init__(self, id):
        self._id = id

        api_url = f"http://api.themoviedb.org/3/movie/{self.id}?api_key={API_KEY}&language=fr"

        response = r.get(api_url).json()
        # print(json.dumps(response, sort_keys=True, indent=4))

        self._title = response['title']
        self._description = response['overview']
        if response['poster_path'] != None:
            self._img = 'https://image.tmdb.org/t/p/w500' + response['poster_path']
        else: 
            self._img = 'https://i.pinimg.com/originals/72/24/f6/7224f6d53614cedbf8cef516b705a555.jpg'
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


    def context(self) -> dict :
        """ Renvoie sous forme de dictionnaire pour pouvoir être utilisé dans les templates.
        In : self
        Out : dictionnaire contenant des informations sur le film
        """

        new_movie = DB_Movie(self.id, self.title, self.description, self.img, self.date)
        new_movie.save()

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "img": self.img,
            "date": self.date,
        }