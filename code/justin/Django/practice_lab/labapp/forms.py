from django.forms import ModelForm
from .models import Priority, Todo

class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = '__all__'

class TodoForm(ModelForm):
    class Meta:

        model = Todo
        fields = '__all__'

class CloseForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('item', 'completed_date')