from django import forms
from .models import BlogPost
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

    # def save(self, commit=True):
    #     user = super(NewUser, self).save(commit-False)
    #     if commit():
    #         user.save
    #     return user

class BlogPost(ModelForm):
    class Meta:
        model = BlogPost
        post = '__all__'
        user = {'user': forms.HiddenInput()}