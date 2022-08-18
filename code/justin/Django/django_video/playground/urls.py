from django.urls import path
from . import views

urlpatterns = [
    path('playground/hello', views.say_hello)
]