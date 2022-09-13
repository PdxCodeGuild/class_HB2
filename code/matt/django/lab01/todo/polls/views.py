from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import TodoItem, Priority
from django.views.decorators.csrf import csrf_protect

def index(request):
    uncompleted_todoitems = TodoItem.objects.order_by('priority')
    context = {'uncompleted_todoitem': uncompleted_todoitems}
    return render(request, 'polls/index.html', context)

@csrf_protect
def todoitem_form(request):
    priorities = Priority.objects.all()
    context = {'priorities': priorities}
    return render(request, 'polls/todoitem_form.html', context)

def save_todo_item(request):
    todo = request.POST.get("tditem")#This is a string
#    print(todo)
    priority_level = request.POST.get('priority')#This is a string
    #print(priority_id)

    #print(request)
    # print(request.POST)
    # print(request.POST.keys())
    # print(dir(request.POST))
    print(type(request))

    p = Priority.objects.create(name=priority_level)

    # print(type(p))
    t = TodoItem.objects.create(text=todo, priority=p)
    return HttpResponseRedirect('/polls/')







