from rest_framework import serializers
from pokemon.models import Pokemon, PokemonType
from django.contrib.auth import get_user_model

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('type',)
        model = PokemonType

class NestedPokemonSerializer(serializers.ModelSerializer)
    class Meta:
        fields = ('name')
        model = Pokemon
class PokemonSerializer(serializers.ModelSerializer):
    type_info = NestedTypeSerializer(many=True, source='types')
    class Meta:
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type_info', 'id')
        model = Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'type', 'pokemon')
        model = PokemonType

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'caught', 'username')
        model = get_user_model()