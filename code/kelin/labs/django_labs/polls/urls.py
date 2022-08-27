from django.urls import path
from .views import register, sign_in, sign_out, user_profile
from django.conf import settings
from django.conf.urls.static import static
from polls import views

# from . import views

app_name = 'polls'

# The manual way
from .views import sign_in, register, sign_out, user_profile
urlpatterns = [
    path('sign_in', sign_in, name='sign_in'),
    path('sign_out', sign_out, name='sign_out'),
    path('register', register, name='register'),
    path('user_profile', user_profile, name='user_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)