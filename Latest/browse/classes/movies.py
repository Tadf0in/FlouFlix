import requests as r
from .config import API_KEY
from browse.models import Movie as DB_Movie
from browse.models import Watchlist as DB_Watchlist


class Movie:
    """
    Passe les informations d'un film récupérées dans l'API TMDB sous forme de classe.
    """
    def __init__(self, id):
        """
        In : id (int) : ID du film dans la BDD (et dans l'API)
        """
        self._id = id

        try:
            # Si dans la BDD
            db = DB_Movie.objects.get(id=id)
            self._title = db.title
            self._description = db.description
            self._img = db.img
            self._date = db.date

            try:
                # Si dans la WatchList
                wl = DB_Watchlist.objects.get(movie=id)
                self.is_in_watchlist = True
            except DB_Watchlist.DoesNotExist:
                # Si pas dans la WatchList
                self.is_in_watchlist = False
            
        except DB_Movie.DoesNotExist:
            # Si pas dans la BDD
            self.is_in_watchlist = False
            self.api() # Récupère les infos dans l'api
            self.to_db('temp') # AJoute dans la BDD

    
    def api(self):
        """ Récupères les informations sur le film dans l'API TMDB
        In : self
        Out : rien
        """
        api_url = f"http://api.themoviedb.org/3/movie/{self.id}?api_key={API_KEY}&language=fr"

        response = r.get(api_url).json()
        # print(json.dumps(response, sort_keys=True, indent=4))

        self._title = response['title']
        self._description = response['overview']
        if response['poster_path'] != None:
            self._img = 'https://image.tmdb.org/t/p/w500' + response['poster_path']
        else: 
            self._img = 'https://i.pinimg.com/originals/72/24/f6/7224f6d53614cedbf8cef516b705a555.jpg'
        if response['release_date'] != "":
            self._date = response['release_date']
        else:
            self._date = "1234-12-12"

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
        self.to_db('clicked')

        return {
            "is_in_watchlist": self.is_in_watchlist,
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "img": self.img,
            "date": self.date,
        }


    def to_db(self, status):
        new_movie = DB_Movie(self.id, self.title, self.description, self.img, self.date, status)
        new_movie.save()