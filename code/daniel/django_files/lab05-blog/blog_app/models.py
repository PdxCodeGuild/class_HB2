from django.db import models

# Create your models here.

class CreateBlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(verbose_name="blog body")
    user = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True) 
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title + ' ' + self.body + ' ' + self.user + ' ' + self.date_created + ' ' + date_edited









