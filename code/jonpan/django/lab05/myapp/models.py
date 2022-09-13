from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    
    class Meta:
        ordering = ["-date_created"]
    
    title = models.CharField(max_length=300, unique=True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
