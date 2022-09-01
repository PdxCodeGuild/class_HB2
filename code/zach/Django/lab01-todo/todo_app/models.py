from django.db import models

# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text