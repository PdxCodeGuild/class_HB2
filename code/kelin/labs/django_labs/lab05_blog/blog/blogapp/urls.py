# Create the following pages:

# Profile /profile/
# show a list of the user's own posts, only showing the title of each
# Create Post /create/
# form for creating a new post


from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [    
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.loginto, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name='create'),
    path('edit/', views.edit, name='edit',),
]