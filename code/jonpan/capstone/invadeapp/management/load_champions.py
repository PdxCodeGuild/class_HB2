from django.core.management.base import BaseCommand
from invadeapp.models import Champions
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Champions.objects.all().delete()
        f = open('getchampions.json')
        champ_list = json.load(f)
        for champion in champ_list['pokemon']:
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