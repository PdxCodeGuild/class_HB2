from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    
    def __str__(self):
        return self.myfield

LEVEL_OF_PRIORITY = [
    ("low","Low"),
    ("med","Med"),
    ("high","High"),
    ("super high","Super High")
]
class Priority(models.Model):
    name = models.CharField(max_length=200, choices=LEVEL_OF_PRIORITY)

    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    date_completed = models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True)
    priority = models.ForeignKey('Priority', on_delete=models.CASCADE, related_name='ToDoItem')

    def __str__(self):
        return self.text
        

