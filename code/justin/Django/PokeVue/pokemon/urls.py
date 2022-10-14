from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'pokemon'
urlpatterns = [
    path('', views.pokeview, name='pokeview'),
    path('index/', views.pokerend, name='index'),
    path('papi/', views.pokemon, name='papi')
]