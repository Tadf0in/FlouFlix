from django.db import models


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=10, default='new')


class Serie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=10, default='new')