from django.forms import ModelForm
from .models import Shorten
from django import forms

class ShortenForm(ModelForm):
    class Meta:
        model = Shorten
        fields = '__all__'
        widgets = {'shorty': forms.HiddenInput()}
