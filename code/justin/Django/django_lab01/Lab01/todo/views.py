from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem, Priority
from django.urls import reverse
from .forms import PriorityForm, TodoForm, td_form
from django.forms import modelform_factory

# Create your views here.
def index(request):
    todo_items = TodoItem.objects.all()
    prio_items = Priority.objects.all()
    context = {
        'todo_items':todo_items,
        'prio_items':prio_items,
    }
    return render(request, 'todo/index.html', context)

def add(request):
    prio_items = Priority.objects.all()
    todo = request.POST['todo']
    priority = request.POST['priority']
    priority = Priority.objects.get(name=priority)
    for items in prio_items:
        print(items) 
    todolist = TodoItem(text=todo, priority = priority)
    todolist.save()
    return HttpResponseRedirect(reverse('todo:index'))
    
# def todoform(request):
#     if request.method == 'POST':
#         form = td_form(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = td_form
#     return render(request, 'todo/index.html', {'form':form})     

