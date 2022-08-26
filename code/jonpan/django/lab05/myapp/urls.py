from django.urls import path
from .views import sign_in, sign_out

app_name = 'myapp'

urlpatterns = [
    path('sign_in', sign_in, name='sign_in'),
    path('sign_out', sign_out, name='sign_out'),
]

    # path('', index, name='index'),
    # path('profile/', views.profile, name='profile'),
    # path('logout/', views.logout_user, name='logout_user'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login_user, name='login_user'),