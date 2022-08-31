from re import M
from django.db import models

# Create your models here.

class Shorten(models.Model):
    webpage = models.CharField(max_length=1000)
    shorty = models.CharField(max_length=200)

    def __str__(self):
        return self.webpage



