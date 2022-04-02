from django.contrib import admin

# Register your models here.
from .models import Movie, Serie, Watchlist


for model in [Movie, Serie, Watchlist]:
    admin.site.register(model)
