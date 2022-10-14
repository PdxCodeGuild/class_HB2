from rest_framework import viewsets
from .models import Pokemon, PokemonType
from .serializers import PokemonSerializer, TypeSerializer
from django.shortcuts import render

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
class TypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    serializer_class = TypeSerializer

def pokemon(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon
    }
    return render(request, 'index.html', context)

def PokemonSearch(request):
    if 'thingy' in request.GET and request.GET['thingy']:
        pokemon_list = request.GET['thingy']
    else: 
        pokemon_list = Pokemon.objects.filter()