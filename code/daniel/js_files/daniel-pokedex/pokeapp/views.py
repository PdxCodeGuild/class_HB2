from django.shortcuts import render
from .models import MyModel

def pokeview(request):
    myinstances = MyModel.objects.all()
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'pokeapp/pokemontemplate.html', context)