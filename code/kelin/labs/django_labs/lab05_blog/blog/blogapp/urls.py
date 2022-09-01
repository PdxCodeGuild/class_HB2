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


from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [    
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name='create'),
]