from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Todo

# from .todo_app import TodoApp

# def index(request):
#   mytodo = TodoApp.objects.all().values()
#   output = ""
#   for x in mytodo:
#     output += x['item']
#   return HttpResponse(output)
""" this was another way of index """
# def index(request):
#   template = loader.get_template('template1.html')
#   return HttpResponse(template.render())

def index(request):
  # print(f'this is request: {request}')
  print('this is request: ' , request) #use this one as best practice in future
  todo_items_view = Todo.objects.all()
  print(todo_items_view) 
  #<QuerySet [<Todo: Feed Fido>, <Todo: Butter Cat>, <Todo: Figure it out>]>
  
  priority_items_views = Priority.objects.all()
  print(priority_items_views)
  
  context = {
    'tdlist': todo_items_view,
    'prlist': priority_items_views,
  }
  return render(request, 'todo_app/template1.html', context)

def detail(request):
  todo_id = 2
  todo = get_object_or_404(Todo, pk=todo_id)
  print('this is todo: ', todo)
  
