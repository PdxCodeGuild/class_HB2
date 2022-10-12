from django.core.management.base import BaseCommand
from invadeapp.models import Champions
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Champions.objects.all().delete()
        f = open('champions.json')
        champ_list = json.load(f)
        for champion in champ_list:
            key_ext = champ_list[champion]["key"]
            hp_ext = champ_list[champion]["stats"]["hp"]
            print(key_ext)



            Champions.objects.create(
                name = champion, 
                hp = hp_ext,  
            )            
                
