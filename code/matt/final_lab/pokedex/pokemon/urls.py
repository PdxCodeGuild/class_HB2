from django.urls import path
from .views import pokemon
from django.views.generic import TemplateView
app_name = 'pokemon'

urlpatterns = [
    # path('<int:number>/', pokemonProfile, name='pokemon_profile'),
    # path('')
    path('api/list', pokemon, name='listapi'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]