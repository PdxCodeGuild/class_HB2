from django.db import models

# Create your models here.

class PokemonType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pokemon(request):
    number = models.IntegerField() 
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=100)
    image_back = models.CharField(max_length=100)
    types = models.ManyToManyField()

