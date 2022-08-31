from django.urls import path
from . import views

app_name = 'url'

urlpatterns = [
    path('entry', views.shortening, name='entry')
]