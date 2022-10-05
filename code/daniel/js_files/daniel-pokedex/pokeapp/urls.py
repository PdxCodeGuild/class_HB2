from django.urls import path
from . import views

app_name = 'pokeapp'
urlpatterns = [
    path('', views.pokeview, name='pokeview'),
    path('mycreate/', views.mycreate, name='mycreate')
]