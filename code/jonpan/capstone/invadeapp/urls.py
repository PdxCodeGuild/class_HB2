from django.urls import path
from . import views

app_name = 'invadeapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("champions/", views.champions, name="champions"),
]