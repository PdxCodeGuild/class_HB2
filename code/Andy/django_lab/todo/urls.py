from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('myview/' , views.index, name='index'),
    path('save/' , views.save, name='save') 
]