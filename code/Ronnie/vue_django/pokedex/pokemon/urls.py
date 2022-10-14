from django.urls import path
from .views import pokemon_profile

app_name = 'pokemon'

urlpatterns = [
    path('<int:number>/', pokemon_profile, name='pokemon_profile')
]
