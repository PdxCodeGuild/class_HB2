from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import TodoItem, Priority

def myview(request):
    todo_items = TodoItem.objects.all()
    priorities = Priority.objects.all()
    context = {
        'todo_items': todo_items,
        'priorities': priorities
    }
    return render(request, 'myapp/mytemplate.html', context)

def save_todo_items(request):
    todo_items = TodoItem.objects.all()
    priorities = Priority.objects.all()
    context = {
        'todo_items': todo_items,
        'priorities': priorities
    }
    form = request.POST
    print(form)

    for key in form:
        if key.startswith('item'):
            whatever = form.get(key)
            TodoItem.objects.create(item=whatever)
    for key in form:
        if key.startswith('name'):
            whatever = form.get(key)
            Priority.objects.create(name=whatever)

    return HttpResponseRedirect(reverse('myapp:myview'))