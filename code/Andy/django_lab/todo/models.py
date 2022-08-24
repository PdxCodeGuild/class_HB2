from django.db import models
from django.forms import CharField
from django.utils import timezone

class Priority(models.Model): 
    CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )
    
    name = models.CharField(max_length = 200, choices = CHOICES, default ='low', null=True)

    def __str__(self) -> str:
        return f"{self.name}" #migrations only when you change or add a method
 


class Todoitem(models.Model):
    text = models.CharField(max_length =200, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True) #populates it right at the time added 

    def __str__(self) -> str:
        return f'{self.text} created at {self.created_date}'
    



# Create your models here.
