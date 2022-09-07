from django.urls import path
from . import views
# from .views import register

app_name = 'blog_app'
urlpatterns = [

    path('', views.index, name='index'),
    
    

]