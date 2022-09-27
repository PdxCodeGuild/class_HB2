from django.shortcuts import render
from .models import Pokemon
from django.http import JsonResponse
# Create your views here.
def index(request):
    pokemon = Pokemon.objects.all()
    return JsonResponse(pokemon)
