from django.db import models
import datetime

# Create your models here.
choice = [
('high','high'),
('medium','medium'),
('low','low')
]
        
class Priority(models.Model):
    name = models.CharField(
        max_length=200,
        choices=choice)
    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.RESTRICT, related_name='priorities')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text + ' ' + f'{self.priority}' + ' ' + f'{self.date_created}'

#