from django.urls import path, include
from .views import RegisterView, profile_view

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile', profile_view, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]