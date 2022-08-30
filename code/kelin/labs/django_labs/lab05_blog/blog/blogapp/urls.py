# Create the following pages:

# Profile /profile/
# show a list of the user's own posts, only showing the title of each
# Create Post /create/
# form for creating a new post

# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from . import views
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('newpost/', views.newpost, name='newpost')
]
