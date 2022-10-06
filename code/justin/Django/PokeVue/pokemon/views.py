from http.client import HTTPResponse
from django.shortcuts import render
from pokemon.models import Pokemon, PokemonType
from django.http import HttpResponse, JsonResponse
from django.core import serializers

# Create your views here.
def pokeview(request):
    return render(request, "pokemon/poketemp.html")

def pokerend(request):
    return render(request, "pokemon/index.html")


def pokemon(request):
    poke = Pokemon.objects.all()
    responsedata = serializers.serialize('json', poke)

    return JsonResponse(responsedata, safe=False)
