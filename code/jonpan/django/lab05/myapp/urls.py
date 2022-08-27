from django.urls import path
from .views import sign_in, register, sign_out, user_profile

app_name = 'myapp'

urlpatterns = [
    path('sign_in', sign_in, name='sign_in'),
    path('sign_out', sign_out, name='sign_out'),
    path('register', register, name='register'),
    path('user_profile', user_profile, name='user_profile'),
]