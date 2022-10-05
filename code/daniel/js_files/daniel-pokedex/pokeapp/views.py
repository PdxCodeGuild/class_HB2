from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

def pokeview(request):
    myinstances = Pokemon.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'pokeapp/pokemontemplate.html', context)

def mycreate(request):
    print(request.POST)
    return HttpResponse('form received')