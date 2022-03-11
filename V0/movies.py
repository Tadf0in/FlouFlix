from config import API_KEY
import requests as r


class Movie:
    def __init__(self, id):
        self._id = id

        api_url = f"https://api.themoviedb.org/3/movie/{self.id}?api_key={API_KEY}&language=fr"

        response = r.get(api_url).json()
        # print(json.dumps(response, sort_keys=True, indent=4))

        self._title = response['title']
        self._description = response['overview']
        self._img = response['poster_path']
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

# Setters
    @id.setter
    def set_id(self, id):
        self._id = id

    @title.setter
    def set_title(self, title):
        self._title = title
    
    @description.setter
    def set_description(self, description):
        self._description = description
    
    @img.setter
    def set_img(self, img):
        self._img = img
    
    @date.setter
    def set_date(self, date):
        self._date = date
