from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import ToDoItem, Priority, MyModel

def myview(request):
    print("request", request)
    print("type_request", type(request))
    myinstances_view = ToDoItem.objects.all()
    prioritylist_view = Priority.objects.all()

    context = {
        'myinstances_template': myinstances_view,
        'prioritylist_template': prioritylist_view
    }
    return render(request, 'ToDo/mytemplate.html', context)

def mycreate(request):
    print('request.POST', request.POST)
    to_do_text = request.POST['user_input']
    print(to_do_text)
    priority = request.POST['priority']
    p = Priority.objects.create(name=priority)

    newToDo = ToDoItem.objects.create(text=to_do_text, priority=p)
    return HttpResponseRedirect(reverse('todo:myview'))

