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
            attack_ext = champ_list[champion]["info"]["attack"]
            defense_ext = champ_list[champion]["info"]["defense"]
            magic_ext = champ_list[champion]["info"]["magic"]
            difficulty_ext = champ_list[champion]["info"]["difficulty"]
            hp_ext = champ_list[champion]["stats"]["hp"]
            hpperlevel_ext = champ_list[champion]["stats"]["hpperlevel"]
            mp_ext = champ_list[champion]["stats"]["mp"]
            mpperlevel_ext = champ_list[champion]["stats"]["mpperlevel"]
            movespeed_ext = champ_list[champion]["stats"]["movespeed"]
            armor_ext = champ_list[champion]["stats"]["armor"]
            armorperlevel_ext = champ_list[champion]["stats"]["armorperlevel"]
            spellblock_ext = champ_list[champion]["stats"]["spellblock"]
            spellblockperlevel_ext = champ_list[champion]["stats"]["spellblockperlevel"]
            attackrange_ext = champ_list[champion]["stats"]["attackrange"]
            hpregen_ext = champ_list[champion]["stats"]["hpregen"]
            hpregenperlevel_ext = champ_list[champion]["stats"]["hpregenperlevel"]
            mpregen_ext = champ_list[champion]["stats"]["mpregen"]
            mpregenperlevel_ext = champ_list[champion]["stats"]["mpregenperlevel"]
            crit_ext = champ_list[champion]["stats"]["crit"]
            critperlevel_ext = champ_list[champion]["stats"]["critperlevel"]
            attackdamage_ext = champ_list[champion]["stats"]["attackdamage"]
            attackdamageperlevel_ext = champ_list[champion]["stats"]["attackdamageperlevel"]
            attackspeedperlevel_ext = champ_list[champion]["stats"]["attackspeedperlevel"]
            attackspeed_ext = champ_list[champion]["stats"]["attackspeed"]
            # print(key_ext)

            Champions.objects.create(
                key = key_ext,
                name = champion,
                attack = attack_ext,
                defense = defense_ext,
                magic = magic_ext,
                difficulty = difficulty_ext,
                hp = hp_ext,
                hpperlevel = hpperlevel_ext,
                mp = mp_ext,
                mpperlevel = mpperlevel_ext,
                movespeed = movespeed_ext,
                armor = armor_ext,
                armorperlevel = armorperlevel_ext,
                spellblock = spellblock_ext,
                spellblockperlevel = spellblockperlevel_ext,
                attackrange = attackrange_ext,
                hpregen = hpregen_ext,
                hpregenperlevel = hpregenperlevel_ext,
                mpregen = mpregen_ext,
                mpregenperlevel = mpregenperlevel_ext,
                crit = crit_ext,
                critperlevel = critperlevel_ext,
                attackdamage = attackdamage_ext,
                attackdamageperlevel = attackdamageperlevel_ext,
                attackspeedperlevel = attackspeedperlevel_ext,
                attackspeed = attackspeed_ext,
            )            
                