from rest_framework import viewsets
from .models import Pokemon, PokemonType
from .serializers import PokemonSerializer, TypeSerializer

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
class TypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    serializer_class = TypeSerializer

#def pokemon(request):
#    pokemon = Pokemon.objects.all()
#    context = {
#        'pokemon': pokemon
#    }
#    return render(request, 'pokeapp/pokemon.html', context)