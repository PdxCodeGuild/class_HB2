from unicodedata import name
from django.db import models

# Create your models here.
class Priority(models.Model):
    name = models.CharField(
        max_length=200,
        # choices=[
        #     ('high','high'),
        #     ('medium','medium'),
        #     ('low','low')
        #     ]
        )
    def __str__(self):
        return self.name

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.RESTRICT, related_name='priorities')

    def __str__(self):
        return self.text + ' ' + f'{self.priority}'