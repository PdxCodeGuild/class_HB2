from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon, PokemonType
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        with open('pokemon.json','r') as f:
            response = f.read()
            pokemon_list = json.loads(response)
            for pokemon in pokemon_list['pokemon']:
                current_pokemon = Pokemon.objects.create(
                    number = pokemon['number'],
                    name = pokemon['name'],
                    height = int(pokemon['height'])/10,
                    weight = int(pokemon['weight'])/10,
                    image_front = pokemon['image_front'],
                    image_back = pokemon['image_back'],
                    types = ', '.join(pokemon['types']),        
                )

                for type in pokemon['types']:                 
                    try:
                        current_type = PokemonType.objects.get(name = type)                        
                    except PokemonType.DoesNotExist:
                        current_type = PokemonType.objects.create(name = type)                           
                    current_pokemon.PokemonType.add(current_type)                               
                    current_pokemon.save()


# f = open('pokemon.json')  # open the file
# contents = json.load(f)  # read the contents
# print(contents)
# Pokemon.objects.create(
#                 value_1 = file['value_1']
#                  value_1 = file['value_1']
#             )

# go through for loop to get all the attributes I'm trying to store for each pokemon
# import models from Pokemon