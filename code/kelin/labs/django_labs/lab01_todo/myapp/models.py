# from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    
    def __str__(self):
        return self.myfield

class Priority(models.Model):
    BOOL_CHOICES = [(1,'High'),(2,'Medium'),(3,'Low')]
    name = models.BooleanField(choices=BOOL_CHOICES) # Priority (high, medium, low) dropdown

class ToDoItem(models.Model):
    text = models.CharField(max_length=200) # ToDoItem text
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE) # Foriegn Key to Priority
    created_date = models.DateTimeField(null=True) # New ToDoItem null completed date