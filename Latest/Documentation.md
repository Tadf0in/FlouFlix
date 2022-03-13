# Documentation

### Présentation

FlouFlix est un site internet présentant un catalogue complet de Film et séries où l'on peut avoir une seule WatchList regroupant toutes les plateformes VOD.


### Changelog

- V2 :
  * Ajout d'un favicon (+ gestion du dossier 'static')
  * L'application django 'movie' devient l'application plus générale 'browse' qui ne comprendra pas que les films
  * Création des classes : Serie, Season et Episode
  * Ajout de la page serie/$id$ qui récupère les informations sur une série (dont l'id est précisé dans l'url) et les affiches
- V1 :
  * Création de l'application django intitulée 'movie'
  * Déplacement de la classe Movie dans un dossier classes
  * AJout de la page movie/$id$ qui récupère les informations sur un film (dont l'id est précisé dans l'url) et les affiches
- V0 :
  * Initialisation du projet django
  * Création de la classe Movie, qui récupère des informations sur un film


### Conception

Le site est géré avec Django.
<br>
Toutes les informations sont récupérées via l'API TMDB.
