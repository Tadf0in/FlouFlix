# Documentation

### Présentation

FlouFlix est un site internet présentant un catalogue complet de Film et séries où l'on peut avoir une seule WatchList regroupant toutes les plateformes VOD.


### Changelog

- V2 :
  * Ajout d'un favicon (+ gestion du dossier 'static')
  * L'application django 'movie' devient l'application plus générale 'browse' qui ne comprendra pas que les films
- V1 :
  * Création de l'application django intitulée 'movie'
  * Déplacement de la classe Movie dans un dossier classes
  * La page movie/ récupère les informations sur un film (dont l'id est précisé dans l'url) et les affiches
- V0 :
  * Initialisation du projet django
  * Création de la classe Movie


### Conception

Le site est géré avec Django.
<br>
Les informations sur un films sont récupérées dans l'API TMDB.
