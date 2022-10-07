from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse
from .models import Pokemon
from django.core import serializers


def pokeview(request):
    myinstances = Pokemon.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'pokeapp/pokemontemplate.html', context)

def pokemon(request):
    listPokemon = Pokemon.objects.all()
    listResponse = serializers.serialize('json', listPokemon)

    return JsonResponse(listResponse, safe=False)


