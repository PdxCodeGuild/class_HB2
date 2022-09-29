from django.urls import path
from . import views

app_name = 'pokeapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon', views.pokemon, name='pokemon'),
    path('pokemon/<str:search>/', views.fetchPokemon, name='search'),
    path('pokemon/<int:page>/', views.pokemon, name='pokemon')
]