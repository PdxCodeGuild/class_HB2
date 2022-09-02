from django.urls import path
from . import views
# from .views import register

app_name = 'blog_app'
urlpatterns = [

    path('index/', views.index, name='index'),
    
    

]