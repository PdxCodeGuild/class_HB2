# from django.db import models

# Create your models here.
from django.db import models

# class MyModel(models.Model):
#     myfield = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.myfield

class Priority(models.Model):
    # BOOL_CHOICES = [(1,'High'),(2,'Medium'),(3,'Low')]
    name = models.CharField(max_length=200) # Priority (high, medium, low) dropdown
    def __str__(self):
        return self.name

class ToDoItem(models.Model): 
    """
    Created Doc String
    """
    text = models.CharField(max_length=200) # ToDoItem text
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE) # Foriegn Key to Priority
    created_date = models.DateTimeField(auto_now_add=True) # Created date

    def __str__(self):
        return self.text

        # return self.text, self.priority, self.created_date
        # return self.text, self.priority, self.created_date
        # return self.text, self.priority, self.created_date