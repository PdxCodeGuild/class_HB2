from django import forms 
from .models import BlogPost
from django.forms import ModelForm

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        # fields = ('title', 'body')
        widgets = {'user': forms.HiddenInput()} #wiget helps handle rendering of HTML and extraction of data from GET/POST dic