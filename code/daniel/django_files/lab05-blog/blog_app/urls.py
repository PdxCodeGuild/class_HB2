from django.urls import path
from . import views
from .views import register_view, index_view, login_view, create_view, logout_view

app_name = 'blog_app'
urlpatterns = [
    path('', index_view, name='index'),
    path('register-view/', register_view, name='register_view'),
    path('login-view/', login_view, name='login_view'),
    path('create-view/', create_view, name='create_view'),
    path('logout-view/', logout_view, name='logout_view'),
    # path('index/', index_view, name='index'),
]


