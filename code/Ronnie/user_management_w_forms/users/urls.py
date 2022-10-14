from django.urls import path, include
from .views import profile, register


app_name = "users"

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('register/', register, name="register"),
    path('accounts/', include("django.contrib.auth.urls")),
]
