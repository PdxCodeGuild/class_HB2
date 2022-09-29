from rest_framework import viewsets
from django.shortcuts import render
from django.contrib.auth import get_user_model
from pokemon.models import Pokemon, PokemonType
from .serializers import PokemonSerializer, TypeSerializer, CustomUserSerializer
from .permissions import IsAuthorOrReadyOnly

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
   
class TypeViewSet(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    serializer_class = TypeSerializer

class PokemonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentUser(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user