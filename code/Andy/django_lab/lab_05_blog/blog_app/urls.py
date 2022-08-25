from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
]