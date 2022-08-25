from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('myview', views.myview, name='myview'),
]

