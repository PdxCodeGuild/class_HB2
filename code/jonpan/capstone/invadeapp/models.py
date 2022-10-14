from django.db import models

class Champions(models.Model):
    key = models.IntegerField() 
    name = models.CharField(max_length=200)
    attack = models.IntegerField() 
    defense = models.IntegerField() 
    magic = models.IntegerField() 
    difficulty = models.IntegerField() 
    hp = models.FloatField()
    hpperlevel = models.FloatField()
    mp = models.FloatField()
    mpperlevel = models.FloatField()
    movespeed = models.FloatField()
    armor = models.FloatField()
    armorperlevel = models.FloatField()
    spellblock = models.FloatField()
    spellblockperlevel = models.FloatField()
    attackrange = models.FloatField()
    hpregen = models.FloatField()
    hpregenperlevel = models.FloatField()
    mpregen = models.FloatField()
    mpregenperlevel = models.FloatField()
    crit = models.FloatField()
    critperlevel = models.FloatField()
    attackdamage = models.FloatField()
    attackdamageperlevel = models.FloatField()
    attackspeedperlevel = models.FloatField()
    attackspeed = models.FloatField()

    def __str__(self):
        return self.name