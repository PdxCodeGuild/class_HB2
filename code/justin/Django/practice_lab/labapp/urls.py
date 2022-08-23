from django.urls import path
from . import views

app_name = 'labapp'
urlpatterns = [
    path('todo/', views.todo, name='todo'),
    path('close/', views.close, name='close' )
]