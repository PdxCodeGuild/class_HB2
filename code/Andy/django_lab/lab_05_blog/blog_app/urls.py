from django.urls import path
from . import views
# from .views import register

app_name = 'blog_app'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
]