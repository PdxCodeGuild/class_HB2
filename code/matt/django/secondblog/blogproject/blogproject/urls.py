"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    #django authentication system. Has a package inside of it that will take care of all our urls for us
    #Simply put, beacuse of this, we do not need a login page, logout page, registration page, etc... it will handle those urls for us for the most part
    path('loginapp/', include('django.contrib.auth.urls')),
    #Why two urls that point to the same place? First: The order of operations is important, so we need this one listed first
    #because django will try to use these authentication urls that come with this package and if it see something else it needs to 
    #know where to go, and in that case we have it pointed at our loginapp.urls
    path('loginapp/', include('loginapp.urls')),
]
