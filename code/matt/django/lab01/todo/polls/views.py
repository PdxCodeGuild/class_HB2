from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import TodoItem, Priority
from django.views.decorators.csrf import csrf_protect

def index(request):
    uncompleted_todoitem = TodoItem.objects.order_by('priority')[:5]
    context = {'uncompleted_todoitem': uncompleted_todoitem}
    return render(request, 'polls/index.html', context)

@csrf_protect
def todoitem_form(request):
    return render(request, 'polls/todoitem_form.html')

def save_todo_item(request):
    todo = request.POST.get("tditem")
    priority_id = request.POST.get('priority')
    priority = Priority.objects.get(id=priority_id)
    new_todoitem = TodoItem(text=todo, priority=priority)
    new_todoitem.save()
    return HttpResponseRedirect('/polls/')







