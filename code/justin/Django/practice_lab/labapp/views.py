from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Priority, Todo
from .forms import PriorityForm, TodoForm

def todo(request):
    todos = Todo.objects.all().values_list('item',flat=True)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()
            return HttpResponseRedirect(reverse('labapp:todo'))
    else:
        form = TodoForm()
    context = {
        'form':form,
        'todos':todos
    }
    return render(request, 'labapp/todo.html', context)

# def item(request):
#     todos = Todo.objects.all()
#     context = {
#         'todos':todos
#     }

#     return render(request, 'labapp/todo.html', context)
    # instances = Priority.objects.all()
    # context = {
    #     'instances':instances
    # }
    # return render(request, 'labapp/todo.html', context)
