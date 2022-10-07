from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        Pokemon.objects.all().delete()

        f = open('pokemon.json')

        poke_balls = json.load(f)

        for pokemon in poke_balls['pokemon']:
        
            name = pokemon.get('name')
            number = int(pokemon.get('number'))
            height = float(pokemon.get('height'))
            weight = float(pokemon.get('weight'))
            image_front = pokemon.get('image_front')
            image_back = pokemon.get('image_back')

            pokemon_obj = Pokemon.objects.create(

                number = number,
                name = name,
                height = height,
                weight = weight,
                image_front = image_front,
                image_back = image_back,

            
            )
            
           


            f.close()

