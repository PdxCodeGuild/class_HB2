from django.urls import URLPattern, path 

from . import views

app_name = 'users'
urlpatterns=[
    path('register/', views.register, name='register'),
    path('profile/<str:username>/',views.profile, name='profile' ),
    path('login/', views.login, name='login'),
    path('logout-user/', views.logout_user, name='logout_user'),

]