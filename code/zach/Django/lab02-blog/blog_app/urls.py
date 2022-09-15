from django.urls import path
from .views import create_post

app_name = 'blog_app'

urlpatterns = [
    path('create_post/', create_post, name='create_post'),
]