from django.contrib import admin

# Register your models here.
from .models import Movie, Serie


for model in [Movie, Serie]:
    admin.site.register(model)
