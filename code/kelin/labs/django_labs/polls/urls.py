from django.urls import path
from .views import sign_in, sign_out
# from . import views

app_name = 'polls'

urlpatterns = [
    # path('', views.index, name='index'),
    path('sign_in', sign_in, name='sign_in'),
    path('sign_out', sign_out, name='sign_out')
]