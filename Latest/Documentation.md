# Documentation

### Présentation

FlouFlix est un site internet présentant un catalogue complet de Film et séries où l'on peut avoir une seule WatchList regroupant toutes les plateformes VOD.


### Changelog

- V1 :
  * Création des classes : Serie, Season et Episode
  * Ajout de la page serie/$id$ qui récupère les informations sur une série (dont l'id est précisé dans l'url) et les affiches
  * Ajout d'un favicon (+ gestion du dossier 'static')
- V0 :
  * Initialisation du projet django
  * Création de l'application django intitulée 'movie'
  * Création de la classe Movie
  * Ajout de la page movie/$id$ qui récupère les informations sur un film (dont l'id est précisé dans l'url) et les affiches


### Conception

Le site est géré avec Django.
<br>
Les informations sur un film sont récupérées dans l'API TMDB.
