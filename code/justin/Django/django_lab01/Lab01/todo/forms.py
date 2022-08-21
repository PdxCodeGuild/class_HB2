from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms import modelform_factory

from .models import TodoItem, Priority

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'

# TodoForm = modelform_factory(TodoItem, fields='__all__')

class PriorityForm():
    class Meta:
        model = Priority
        fields = '__all__'





