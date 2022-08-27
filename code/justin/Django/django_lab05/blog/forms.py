from django import forms
from .models import BlogPost
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}
