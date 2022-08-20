from django.db import models

PRIORITY_CHOICES = [
    ('low', 'LOW'),
    ('medium', 'MEDIUM'),
    ('high', 'HIGH'),
]

class Priority(models.Model):

    name = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default='low',
    )

    def __str__(self):
        return self.name

# title = models.CharField(max_length=200)

class TodoItem(models.Model):
    item = models.CharField(max_length=200, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name="Priority", null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.item
