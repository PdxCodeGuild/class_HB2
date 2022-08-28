from django.db import models

# Create your models here.

class CreateBlogPost(models.Model):
    body = models.TextField(verbose_name="blog body")
    
    def __str__(self):
        return self.body