from .models import Pokemon, PokemonType
from rest_framework import serializers

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = PokemonType

class PokemonSerializer(serializers.ModelSerializer):
    type_info = NestedTypeSerializer(many=True, source='types')
    
    class Meta:
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type_info',)
        model = Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = PokemonType