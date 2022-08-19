from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem, Priority

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
    # prio = Priority(name=priority)
    for items in prio_items:
        print(items) 
    todolist = TodoItem(text=todo, priority = priority)
    todolist.save()
    return HttpResponseRedirect(reverse('todo:index'))
    
