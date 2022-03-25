import requests as r
import json
from .config import API_KEY
from browse.models import Serie as DB_Serie


class Serie:
    """
    Passe les informations d'une série récupérées dans l'API TMDB sous forme de classe.
    """
    def __init__(self, id):
        self._id = id

        try:
            db = DB_Serie.objects.get(id=id)
            self._name = db.name
            self._description = db.description
            self._img = db.img
            self._date = db.date
            self._no_seasons = db.no_seasons
            self._no_episodes = db.no_episodes
            
        except DB_Serie.DoesNotExist:
            self.api()


    def api(self):
        api_url = f"http://api.themoviedb.org/3/tv/{self.id}?api_key={API_KEY}&language=fr"

        response = r.get(api_url).json()
        # print(json.dumps(response, sort_keys=True, indent=4))

        self._name = response['name']
        self._description = response['overview']
        if response['poster_path'] != None:
            self._img = 'https://image.tmdb.org/t/p/w500' + response['poster_path']
        else: 
            self._img = 'https://i.pinimg.com/originals/72/24/f6/7224f6d53614cedbf8cef516b705a555.jpg'
        self._date = response['first_air_date']
        self._no_seasons = response['number_of_seasons']
        self._no_episodes = response['number_of_episodes']

# Getters
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description

    @property
    def img(self):
        return self._img

    @property
    def date(self):
        return self._date

    @property
    def no_seasons(self):
        return self._no_seasons

    @property
    def no_episodes(self):
        return self._no_episodes

    
    def context(self) -> dict :
        """ Renvoie sous forme de dictionnaire pour pouvoir être utilisé dans les templates.
        In : self
        Out : dictionnaire contenant des informations sur la série
        """
        self.to_db()

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "img": self.img,
            "date": self.date,
            "no_seasons": self.no_seasons,
            "no_episodes": self.no_episodes,
        }

    
    def to_db(self):
        new_serie = DB_Serie(self.id, self.name, self.description, self.img, self.date, self.no_seasons, self.no_episodes)
        new_serie.save()



class Season:
    """
    Passe les informations d'une saison récupérées dans l'API TMDB sous forme de classe.
    """
    def __init__(self, serie_id, num):
        self._serie = Serie(serie_id)
        self._serie_id = self.serie.id
        self._num = num

        api_url = f"http://api.themoviedb.org/3/tv/{self.serie_id}/season/{self.num}?api_key={API_KEY}&language=fr"

        response = r.get(api_url).json()
        # print(json.dumps(response, sort_keys=True, indent=4))

        self._name = response['name']
        self._description = response['overview']
        self._img = 'https://image.tmdb.org/t/p/w500' + response['poster_path']
        self._date = response['air_date']

        self._episodes = []
        for episode in response['episodes']:
            self._episodes.append(Episode(self.serie_id, num, episode['episode_number']))

# Getters
    @property
    def serie(self):
        return self._serie

    @property
    def serie_id(self):
        return self._serie_id

    @property
    def num(self):
        return self._num

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description

    @property
    def img(self):
        return self._img

    @property
    def date(self):
        return self._date

    @property
    def episodes(self):
        return self._episodes

    
    def context(self) -> dict :
        """ Renvoie sous forme de dictionnaire pour pouvoir être utilisé dans les templates.
        In : self
        Out : dictionnaire contenant des informations sur la saison
        """
        return {
            "serie": self.serie,
            "serie_id": self.serie_id,
            "num": self.num,
            "name": self.name,
            "description": self.description,
            "img": self.img,
            "date": self.date,
            "episodes": self.episodes,
        }



class Episode:
    """
    Passe les informations d'un épisode récupérées dans l'API TMDB sous forme de classe.
    """
    def __init__(self, serie_id, season_num, episode_num):
        self._serie_id = serie_id
        self._season_num = season_num
        self._episode_num = episode_num

        api_url = f"http://api.themoviedb.org/3/tv/{self.serie_id}/season/{self.season_num}/episode/{self.episode_num}?api_key={API_KEY}&language=fr"
        print(api_url)

        response = r.get(api_url).json()
        # print(json.dumps(response, sort_keys=True, indent=4))

        self._name = response['name']
        self._description = response['overview']
        self._img = 'https://image.tmdb.org/t/p/w500' + response['still_path']
        self._date = response['air_date']

# Getters
    @property
    def serie_id(self):
        return self._serie_id

    @property
    def season_num(self):
        return self._season_num

    @property
    def episode_num(self):
        return self._episode_num

    @property
    def name(self):
        return self._name
    
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
        Out : dictionnaire contenant des informations sur l'épisode
        """
        return {
            "serie_id": self.serie_id,
            "season_num": self.season_num,
            "episode_num": self.episode_num,
            "name": self.name,
            "description": self.description,
            "img": self.img,
            "date": self.date,
        }