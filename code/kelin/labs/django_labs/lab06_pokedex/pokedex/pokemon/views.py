from django.shortcuts import render
from rest_framework import viewsets
from pokemon.models import Pokemon, PokemonType
from .serializer import PokemonSerializer, TypeSerializer

# Create your views here.

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    searlizer_class = TypeSerializer