from django.db import models
from django.contrib.auth.models import User

# Create the following model:

# BlogPost
# title (CharField)
# body (TextField)
# user (ForeignKey to django.contrib.auth.models.User)
# public (BooleanField)
# date_created (DateTimeField with auto_now_add=True)
# date_edited (DateTimeField with auto_now=True)


class BlogPost:
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title