from django.urls import path
from . import views
from .views import register_view, profile_view, login_view, create_view

app_name = 'blog_app'
urlpatterns = [
    path('profile-page', profile_view, name='profile'),
    path('register-page', register_view, name='register'),
    path('login-page', login_view, name='login'),
    path('create-page', create_view, name='create'),
    # path('index/', index_view, name='index'),
]


