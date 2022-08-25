from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title



# Create your models here.
