from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('mycreate/', views.mycreate, name='mycreate')
]