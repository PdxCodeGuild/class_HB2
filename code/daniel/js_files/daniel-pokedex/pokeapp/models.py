from django.db import models

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.CharField(max_length=200)


