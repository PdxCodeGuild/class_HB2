from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    # path('', views.index, name='index'),
    path('todo/', views.todo, name='todo'),
    path('add/', views.add, name='add')
]