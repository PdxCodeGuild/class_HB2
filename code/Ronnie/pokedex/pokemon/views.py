from django.shortcuts import render
from .models import Pokemon
# Create your views here.
def index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemon':pokemon})
