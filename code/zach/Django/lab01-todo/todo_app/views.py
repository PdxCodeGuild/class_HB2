from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from . import models

# Create your views here.
def index_view(request): 
    todo_list = models.ToDoItem.objects.all()
    context = {
        'todo_list_context': todo_list
    }
    return render(request, 'todo_app/index.html', context)

def save_todo_item(request):
    todo_dict = request.POST
    todo_string = todo_dict['todo_name']
    priority_id = int(request.POST['priority'])
    priority_object = get_object_or_404(models.Priority, pk=priority_id)
    todo_object = models.ToDoItem.objects.create(text=todo_string, priority=priority_object)
    print(priority_object, todo_object)
    return HttpResponseRedirect(reverse('todo_app:index_name'))
    