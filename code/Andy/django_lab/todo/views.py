from django.shortcuts import render
from django.http import HttpResponse
from .models import Todoitem, Priority # to get both functions from models
# Create your views here.

# def myview(request):
#     return HttpResponse('hello world! Youre at the todo index.')

def index(request):
    todo_item = Todoitem.objects.all()
    pri_item = Priority.objects.all()

    context = {
        'todo_item': todo_item,
        'pri_item': pri_item
    } 

    return render(request, 'todo/index.html', context)
