from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)
    


