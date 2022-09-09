# todo/todo_app/models.py
from django.db import models
from django.urls import reverse
from django.utils import timezone

def d_plus_seven():
    return timezone.now() + timezone.timedelta(days=7)
# Create your models here.

class Todo(models.Model):
    item = models.CharField(max_length=255)
    creation = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(default=d_plus_seven)
    

    def __str__(self):
        return self.item
        

# class Priority(models.Model):
#     level = {
#         'low': models.ForeignKey(),
#         'medium': models.ForeignKey(),
#         'high': models.ForeignKey()
#     }
#     pass

# class Level(models.Model):
#     priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    # level = {
    #     'low': models.ForeignKey(),
    #     'medium': models.ForeignKey(max_length=8),
    #     'high': models.ForeignKey(max_length=8)
    # }

    # def __str__(self):
    #     return self.level
