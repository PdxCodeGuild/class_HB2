from xmlrpc.client import Boolean
from django.db import models

# Create your models here.

# Create the following model:

# BlogPost
# title (CharField)
# body (TextField)
# user (ForeignKey to django.contrib.auth.models.User)
# public (BooleanField)
# date_created (DateTimeField with auto_now_add=True)
# date_edited (DateTimeField with auto_now=True)

class BlogPost(models.Model):
    title =
    body =
    user = ForeignKey
    public = BooleanField
    date_created = DateTimeField, auto_now_add=True
    date_edited = DateTimeField, auto_now=True
    