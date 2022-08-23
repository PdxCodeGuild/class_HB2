# from django.shortcuts import render

from django.urls import reverse
# Create your views here.

# from django.http import HttpResponse

# def myview(request):
#     return HttpResponse('hello world!')

from django.shortcuts import render
from django.http import HttpResponseRedirect

from code.kelin.labs.django_labs.lab01_todo import myapp
from .models import Priority, ToDoItem

# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def todo(request):
    todo_items = ToDoItem.objects.all()
    print("To do list", todo_items)
    context = {
        'todos_template': todo_items
    }
    return render(request, 'myapp/todo.html', context)

def add(request):
    # print("Keys", request.POST.keys())
    todo = request.POST['todo']
    priority = request.POST['priority']
    # print()
    # print(todo, priority)
    priority = Priority(name=priority)
    priority.save()
    todo = ToDoItem(text=todo, priority=priority)
    # print("Todo entry", todo)
    todo.save()
    return HttpResponseRedirect('myapp:add/todo')