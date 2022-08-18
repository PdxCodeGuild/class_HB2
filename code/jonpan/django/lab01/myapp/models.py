from django.db import models

# Create your models here.

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    
    def __str__(self):
        return self.myfield


class MyModel2(models.Model):
    PRIORITY_CHOICES = (
    ('low', 'LOW'),
    ('medium', 'MEDIUM'),
    ('high', 'HIGH'),
    )
    
    myfield = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='low')

    def __str__(self):
        return self.myfield
