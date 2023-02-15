from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda/', views.search, name='search'),
    path('decks/', views.decks, name='decklists'),
    path('decklist/',views.decklist, name="list"),
]