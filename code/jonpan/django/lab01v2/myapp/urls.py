from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('myview/', views.myview, name='myview'),
    path('save_todo_items/', views.save_todo_items, name='save_todo_items')
]