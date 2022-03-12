from django.urls import path
from . import views

urlpatterns = [
    path('movie/<int:id>/', views.movie, name='browse-movie'),
]