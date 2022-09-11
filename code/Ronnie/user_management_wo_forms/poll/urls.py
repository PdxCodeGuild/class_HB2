from django.urls import path
from .views import register, sign_in, sign_out, user_profile

app_name = 'poll'

urlpatterns = [
    path('sign_in', sign_in, name='sign_in'),
    path('sign_out', sign_out, name='sign_out'),
    path('register', register, name='register'),
    path('user_profile', user_profile, name='user_profile'),
]
