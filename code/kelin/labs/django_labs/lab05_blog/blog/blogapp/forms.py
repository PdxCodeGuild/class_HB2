from django import forms
from .models import BlogPost
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUser(UserCreationForm):
    class Meta:
        model = User
        login = ('username','password','reenter')

class BlogPost(ModelForm):
    class Meta:
        model = BlogPost
        post = '__all__'
        user = {'user': forms.HiddenInput()}