from django.urls import path
from . import views
from .views import register_view, profile_view

app_name = 'blog_app'
urlpatterns = [
    path('profile-page', profile_view, name='profile'),
    path('register-page', register_view, name='register'),
    # path('index/', index_view, name='index'),
]


