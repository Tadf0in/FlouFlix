from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='browse'),

    path('popular/', views.popular, name='browse-popular'),
    path('latest/', views.latest, name='browse-latest'),

    path('movie/<int:id>/', views.movie, name='browse-movie'),
    path('serie/<int:id>/', views.serie, name='browse-serie'),

    path('serie/<int:serie_id>/season/<int:num>', views.season, name='browse-season'),
    path('serie/<int:serie_id>/S<int:season_num>', views.season, name='browse-season'),
    
    # path('serie/<int:serie_id>/S<int:season_num>E<int:episode_num>', views.episode, name='browse-episode'),
    # path('serie/<int:serie_id>/season/<int:season_num>/episode/<int:episode_num>', views.episode, name='browse-episode'),

    path('watchlist/', views.watchlist, name="watchlist"),

    path('search/', views.search, name="search"),

    path('watch/movie/<int:id>/', views.watch_movie, name="watch"), 
    path('watch/serie/<int:id>/S<int:season_num>E<int:episode_num>/', views.watch_serie, name="watch"),   
]