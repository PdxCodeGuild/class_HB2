from rest_framework import viewsets
from pokemon.models import Pokemon, PokemonType
from .serializers import PokemonSerializer, TypeSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
   
class TypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    serializer_class = TypeSerializer