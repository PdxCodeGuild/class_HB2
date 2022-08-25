from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Priority, Todo
from .forms import PriorityForm, TodoForm, CloseForm

def todo(request):
    todos = Todo.objects.all().values_list('item',flat=True)
    todone = Todo.objects.all().values_list('completed_date',flat=True)
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
        'todos':todos,
        'todone':todone,
    }
    return render(request, 'labapp/todo.html', context)

def close(request):
    if request.method == "POST":
        form = CloseForm(request.POST)
        if form.is_valid():
            return render(request, 'labapp/close.html', {'form':form})   
    else:
        print('something went wrong')
    

    return render(request, 'labapp/close.html', {'form':form})


    # return render(request, 'labapp/close.html', context)


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
