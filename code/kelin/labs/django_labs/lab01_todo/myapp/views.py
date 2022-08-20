# from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

# def myview(request):
#     return HttpResponse('hello world!')

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Priority, ToDoItem

# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def todo(request):
    todo_items = ToDoItem.objects.all()
    print("To do list", todo_items)
    context = {
        'todos': todo_items
    }
    return render(request, 'myapp/todo.html', context)

def add(request):
    todo = request.POST['todo']
    priority = request.POST['priority']
    print()
    print(todo, priority)
    # priority_level = Priority(name=priority)
    # priority_level.save()
    # todolist = ToDoItem(text=todo, priority=priority_level)
    # todolist.save()
    return HttpResponseRedirect('myapp/todo.html')