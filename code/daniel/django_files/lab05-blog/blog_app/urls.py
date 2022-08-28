from django.urls import path
from . import views
# from .views import index_view

app_name = 'blog_app'
urlpatterns = [
    path('profile-page/', views.profile_view, name='profile'),
    # path('index/', index_view, name='index'),
]