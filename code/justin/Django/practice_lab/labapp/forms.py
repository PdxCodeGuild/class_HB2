from django.forms import ModelForm
from .models import Priority, Todo
from django import forms

class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = '__all__'

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = (
            'item',
            'importance',        
        )
        

class CloseForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('item', 'completed_date')