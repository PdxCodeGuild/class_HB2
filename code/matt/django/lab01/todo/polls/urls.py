from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('todoitem_form/', views.todoitem_form, name='todoitem_form'),
    path('save_todo_item/', views.save_todo_item, name='save_todo_item'),
]