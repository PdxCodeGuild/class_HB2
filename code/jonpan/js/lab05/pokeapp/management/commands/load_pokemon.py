from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        f = open('pokemon.json')  # open the file
        contents = json.load(f)  # read the contents
        print(contents)


# Pokemon.objects.create(
#                 value_1 = file['value_1']
#                  value_1 = file['value_1']
#             )

# go through for loop to get all the attributes I'm trying to store for each pokemon
# import models from Pokemon
# register model in Admin