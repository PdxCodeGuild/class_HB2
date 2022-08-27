from django.urls import path
from temp import views

app_name = 'temp'
urlpatterns = [
    path('hotorcold/', views.index, name='index')
]