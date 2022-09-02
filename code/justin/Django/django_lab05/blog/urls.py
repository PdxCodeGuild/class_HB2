from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [    
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.logins, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name='create'),
]