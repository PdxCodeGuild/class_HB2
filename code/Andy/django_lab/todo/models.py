from django.db import models
from django.forms import CharField
from django.utils import timezone

class Priority(models.Model): 
    CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )
    
    name = models.CharField(max_length = 200, choices = CHOICES, default ='low')
 


class Todoitem(models.Model):
    text = models.CharField(max_length =200)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True) #populates it right at the time added 

    



# Create your models here.
