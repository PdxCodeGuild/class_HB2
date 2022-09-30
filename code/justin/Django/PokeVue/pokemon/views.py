from http.client import HTTPResponse
from django.shortcuts import render
from pokemon.models import Pokemon, PokemonType
from django.http import HttpResponse, JsonResponse

# Create your views here.
def pokeview(request):
    return render(request, "pokemon/poketemp.html")

def pokemon(request):
    poke = Pokemon.objects.all()
    for p in poke:

        responsedata = {
            'p':p
        }  
    return JsonResponse(request, 'pokemon/index.html',responsedata)
