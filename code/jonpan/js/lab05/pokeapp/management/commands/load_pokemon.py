from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        f = open('pokemon.json')
        poke_balls = json.load(f)
        for pokemon in poke_balls['pokemon']:
            name_ext = pokemon.get('name')
            number_ext = int(pokemon.get('number'))
            height_ext = int(pokemon.get('height'))
            weight_ext = int(pokemon.get('weight'))
            image_front_ext = pokemon.get('image_front')
            image_back_ext = pokemon.get('image_back')

            pokemon_obj = Pokemon.objects.create(
                name = name_ext,
                number = number_ext,
                height = height_ext,
                weight = weight_ext,
                image_back = image_back_ext,
                image_front = image_front_ext,
            )

            print(pokemon_obj.name + ' has been uploaded')

        # f = open("pokemon.json")
        # contents = json.load(f)
        # for x in range(len(contents['pokemon'])):
        #     poke = Pokemon()
        #     poke.number = contents["pokemon"][x]["number"]
        #     poke.name = contents['pokemon'][x]['name']
        #     poke.height = contents["pokemon"][x]["height"] / 10
        #     poke.weight = contents["pokemon"][x]["weight"] / 10
        #     if contents["pokemon"][x]["image_front"] == None:
        #         poke.image_front = "No front image available"
        #     else:
        #         poke.image_front = contents["pokemon"][x]["image_front"]
        #     if contents["pokemon"][x]["image_back"] == None:
        #         poke.image_back = "No back image available"
        #     else:
        #         poke.image_back = contents["pokemon"][x]["image_back"]
        #     poke.save() 

# f = open('pokemon.json')  # open the file
# contents = json.load(f)  # read the contents
# print(contents)
# Pokemon.objects.create(
#                 value_1 = file['value_1']
#                  value_1 = file['value_1']
#             )

# go through for loop to get all the attributes I'm trying to store for each pokemon
# import models from Pokemon