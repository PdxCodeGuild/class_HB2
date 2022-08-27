import datetime
from django.db import models
from django.utils import timezone

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
    body = models.TextField
    user = models.ForeignKey
    public = models.BooleanField
    date_created = models.DateTimeField(auto_now=True)