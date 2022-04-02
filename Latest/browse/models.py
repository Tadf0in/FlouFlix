from django.db import models


"""
AutoField = INT avec AutoIncrement
IntegerField = INT
CharField = VARCHAR
TextField = TEXT
DateFild = DATE

ForeignKey = Clé étrangère

primary_key=True : clé primaire
blank=True : peut être vide
null=True : si vide alors NULL est assigné
max_length=n : définit la taille max d'un VARCHAR
"""


class Movie(models.Model):
    """
    Crée une table 'Movie' dans la base de données
    """
    # Création de chaque colonne de la table
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    img = models.CharField(blank=True, null=True, max_length=100)
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, default='temp')

    class Meta:
        managed = False
        db_table = 'Movie'


class Serie(models.Model):
    """
    Crée une table 'Serie' dans la base de données
    """
    # Création de chaque colonne de la table
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    img = models.CharField(blank=True, null=True, max_length=100)
    date = models.DateField(blank=True, null=True)
    no_seasons = models.IntegerField(blank=True, null=True)
    no_episodes = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, default='temp')

    class Meta:
        managed = False
        db_table = 'Serie'


class Watchlist(models.Model):
    """
    Crée une table 'WatchList' dans la base de données

    Paire (id, null) ou (null, id) pour savoir si l'id est celui d'un film ou d'une série
    """
    # Création de chaque colonne de la table
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey('Movie', null=True, on_delete=models.CASCADE) # clé étrangère : Movie.id
    serie = models.ForeignKey('Serie', null=True, on_delete=models.CASCADE) # clé étrangère : Serie.id

    class Meta:
        managed = False
        db_table = 'WatchList'