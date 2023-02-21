from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda/', views.search, name='search'),
    path('decks/', views.decks, name='decklists'),
    path('decklist/<int:pk>/',views.decklist, name="list"),
    path('detalle/<str:cardnumber>/', views.detalle, name="detalle"),
    path("builder/", views.create_deck, name="builder"),

]