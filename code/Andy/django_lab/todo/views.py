from django.shortcuts import redirect, render   
from django.http import HttpResponse
from .models import Todoitem, Priority # to get both functions from models
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# def myview(request):
#     return HttpResponse('hello world! Youre at the todo index.')

def index(request):
    todo_items = Todoitem.objects.all()
    # pri_item = Priority.objects.all()
    print('todo item', todo_items )
    print('type todo item', type(todo_items))

    context = {
        'todo_item': todo_items,
        # 'pri_item': pri_item
    } 

    return render(request, 'todo/index.html', context)


def save(request):
    form = request.POST
    # print(form)
    todo = form.get('text') #todo from html page. from user
    pri = form.get('name')
    # print(todo)
    # print(pri)
    p = Priority.objects.create(name=pri)
    Todoitem.objects.create(text=todo, priority=p)
    return redirect(reverse('todo:index'))