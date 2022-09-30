from django.urls import path
from .views import pokemonProfile

app_name = 'pokemon'

urlpatterns = [
    path('<int:number>/', pokemonProfile, name='pokemon_profile')
]