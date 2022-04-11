<div align="center"><img src="Latest/doc/img/flouflix.png"></img></div>

## Présentation

FlouFlix est un site internet présentant un catalogue complet de bandes annonces de Film et séries où l'on peut avoir une seule WatchList regroupant tous les films et séries sans se soucier de la plateforme VOD.

<br>

## Prérequis

Sous **browse/classes/** crée un fichier intitulé **config.py** qui contiendra la clé d'api :
<br>
(générable à l'adresse suivante : https://www.themoviedb.org/settings/api)

##### config.py
``` config.py
API_KEY = "" #Entrer la clé d'api ici
```

<br>

Packages python utilisés :
* Django (version 4.0.3) 
 ```bash
 pip install django==4.0.3
 ```
* Requests (version 2.27.1)
 ```bash
 pip install requests==2.27.1
 ```
* Windows Curses (version 2.0.3)
 ```bash
 pip install windows_curses==2.0.3
 ```

## Documentation
[Documentation.md](doc/Documentation.md)

<br>

## Fiches problème

* [Fiche problème 1](doc/fiche_probleme1.md)
* [Fiche problème 2](doc/fiche_probleme2.md)