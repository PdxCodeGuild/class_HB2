from django.db import models
from django.contrib.auth.models import User 
# from django.utils import timezone  
from django.utils.timezone import now


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user') 
    # date_created = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(default=now)
    date_edited = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title



# Create your models here.
