from re import M
from django.db import models

# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=255)

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
