from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
]