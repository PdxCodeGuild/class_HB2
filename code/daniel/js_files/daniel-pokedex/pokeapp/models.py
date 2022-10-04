from django.db import models

class Pokemon(models.Model):
    number = models.CharField(max_length=200)