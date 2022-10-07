from email.policy import default
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
    if request.method == 'GET':
        qball = request.GET.get('name', default=None)
        if qball == None:
            poke = Pokemon.objects.all()
            responsedata = serializers.serialize('json', poke) 
            print('its none just doin it')
        else:
            qball = Pokemon.objects.filter(name = qball)
            responsedata = serializers.serialize('json', qball)
            print(qball)


    return JsonResponse(responsedata, safe=False)

