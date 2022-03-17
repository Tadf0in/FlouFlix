from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='browse'),

    path('<str:filter>/', views.filter, name='browse-filter'),

    path('movie/<int:id>/', views.movie, name='browse-movie'),
    path('serie/<int:id>/', views.serie, name='browse-serie'),

    path('serie/<int:serie_id>/season/<int:num>', views.season, name='browse-season'),
    path('serie/<int:serie_id>/S<int:season_num>', views.season, name='browse-season'),
    
    # path('serie/<int:serie_id>/S<int:season_num>E<int:episode_num>', views.episode, name='browse-episode'),
    # path('serie/<int:serie_id>/season/<int:season_num>/episode/<int:episode_num>', views.episode, name='browse-episode'),
    
]