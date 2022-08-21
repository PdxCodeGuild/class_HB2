from django.db import models
import datetime

# Create your models here.
choice = (
    ('high','high'),
    ('medium','medium'),
    ('low','low'),
)

class Priority(models.Model):
    priority = models.CharField(
        max_length=20,
        choices = choice
        )
    def __str__(self):
        return self.priority

class Todo(models.Model):
    item = models.CharField(max_length=50)
    importance = models.ForeignKey(Priority, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.item + " " + f'{self.importance}' + " " + f'{self.create}'
