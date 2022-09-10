from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class CreateBlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(verbose_name="blog body")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts" )
    public = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True) 
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' ' + self.body + ' ' + str(self.date_created) + ' ' + str(self.date_edited) +  ' ' + str(self.user.username)





#  + self.user.username +



