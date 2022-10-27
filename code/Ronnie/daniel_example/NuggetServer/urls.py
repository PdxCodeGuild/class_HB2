from django.urls import path
from . import views

app_name = 'NuggetServer'
urlpatterns = [
    path('register/', views.register_request, name="register"),
    path('home/', views.myhomepage, name='homepage'),
    path('flash/', views.mycreate, name='FlashWifiNugget'),
    path('database/', views.mycreate, name='MACDatabase'),
]