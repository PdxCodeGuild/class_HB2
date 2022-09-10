from django.db import models

# Create your models here.

class PokemonType(models.Model):
    name = models.CharField(max_length=100)

class Pokemon(models.Model):
    number =
    name = 