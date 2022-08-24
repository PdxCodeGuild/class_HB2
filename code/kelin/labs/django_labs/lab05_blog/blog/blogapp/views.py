from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

# Create the following views:

# Register /register/
# form for creating a new user
# redirect to /profile/ after registering
# Login /login/
# form for logging a user in
# redirect to /profile/ after logging in
# Profile /profile/
# a protected page only logged in users can see
# just show a welcome message for now

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user = User.objects.create_user(username, password)
    new_user.save()
    return HTTPResponse("Thank you for registering")
    
    
def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if request.user is not None:
        login(request, user)
        return HTTPResponse("Logged in")
    else:
        return HTTPResponse(user)