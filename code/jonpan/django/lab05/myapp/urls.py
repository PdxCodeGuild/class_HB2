from django.urls import path
# from .views import sign_in, register, sign_out, user_profile, create, show_the_form, post
from . import views

app_name = 'myapp'

# urlpatterns = [
#     path('sign_in', sign_in, name='sign_in'),
#     path('sign_out', sign_out, name='sign_out'),
#     path('register', register, name='register'),
#     path('user_profile', user_profile, name='user_profile'),
#     path('create/', create, name='create'),
#     path('show-the-form', show_the_form, name='show_the_form'),
#     # path('post_detail', post_detail, name='post_detail'),
# ]

urlpatterns = [
    path('sign_in/', views.sign_in, name="sign_in"),
    path('register/', views.register, name="register"),
    path('profile/', views.user_profile, name="user_profile"),
    path('sign_out/', views.sign_out, name="sign_out"),
    path('create/', views.create, name="create"),
    path('blogpost/<int:blog_id>', views.view_blog, name='view_blog'),
]