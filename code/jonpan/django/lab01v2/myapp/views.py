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
    # todo_items = TodoItem.objects.all()
    # priorities = Priority.objects.all()
    # context = {
    #     'todo_items': todo_items,
    #     'priorities': priorities
    # }
    form = request.POST
    # print(form.keys())

    priority_value = form['name']
    todoitem_text = form['item']

    priority_object = Priority.objects.create(name=priority_value)
    TodoItem.objects.create(item=todoitem_text, priority=priority_object)

    # for key in form:
    #     if key.startswith('name'):
    #         priority_word = form.get(key)
    #         Priority.objects.create(name=priority_word)

    # for key in form:
    #     if key.startswith('item'):
    #         todoitem_text = form.get(key)
    #         TodoItem.objects.create(item=todoitem_text)

    return HttpResponseRedirect(reverse('myapp:myview'))