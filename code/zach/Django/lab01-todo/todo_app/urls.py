from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('index-url/', views.index_view, name="index_name"),
    path('save-todo/', views.save_todo_item, name="save_name")
]