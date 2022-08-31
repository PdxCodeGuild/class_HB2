from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'url'

urlpatterns = [
    path('entry', views.shortening, name='entry'),
    path('result', TemplateView.as_view(template_name="result.html"), name='result'),

]