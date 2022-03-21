from django.db import models


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    img = models.CharField(blank=True, null=True, max_length=100)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Movie'


class Serie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    img = models.CharField(blank=True, null=True, max_length=100)
    date = models.DateField(blank=True, null=True)
    no_seasons = models.IntegerField(blank=True, null=True)
    no_episodes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Serie'


class Watchlist(models.Model):
    movie_id = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)
    serie_id = models.ForeignKey(Serie, null=True, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'WatchList'
        unique_together = (("movie_id", "serie_id"),)