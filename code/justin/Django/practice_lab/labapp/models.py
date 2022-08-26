from django.db import models
import datetime

# Create your models here.


class Priority(models.Model):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    choice = (
    (HIGH,'high'),
    (MEDIUM,'medium'),
    (LOW,'low'),)
    priority = models.CharField(
        max_length=20,
        choices = choice
        )
    def __str__(self):
        return self.priority

class Todo(models.Model):
    item = models.CharField(max_length=50)
    importance = models.ForeignKey(Priority, on_delete=models.RESTRICT, choices=Priority.choice)
    create = models.DateTimeField(auto_now= True)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.item + " " + f'{self.importance}' + " " + f'{self.create}'
