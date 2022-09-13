from django.urls import path, include
from .views import register, profile_view

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]