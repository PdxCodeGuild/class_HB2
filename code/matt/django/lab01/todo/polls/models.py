from django.db import models

class Priority(models.Model):
    PRIORITY_NUMS = [
        ('low', 'Low'),
        ('med', 'Medium'),
        ('high', 'High'),
        ('imp', 'MOST IMPORTANT')
    ]
    name = models.CharField(max_length=200, choices=PRIORITY_NUMS, default="low", null=True)
    

    def __str__(self):
        return f'{self.name}'

class TodoItem(models.Model):
    text = models.CharField(max_length=200, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.text


# Create your models here.

