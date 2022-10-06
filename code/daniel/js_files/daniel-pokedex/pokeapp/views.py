from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Pokemon

def pokeview(request):
    myinstances = Pokemon.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'pokeapp/pokemontemplate.html', context)

def mycreate(request):
    myfield = request.POST['myfield']
    mymodel = Pokemon(myfield=myfield)
    mymodel.save()
    return HttpResponseRedirect(reverse('pokeapp:pokeview'))