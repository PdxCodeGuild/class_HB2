from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    # path('', views.index, name='index'),
    path('myview/', views.myview, name='myview'),
    path('mycreate/', views.mycreate, name='mycreate')
]