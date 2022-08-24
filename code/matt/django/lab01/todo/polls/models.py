from django.db import models

class Priority(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


# Create your models here.

