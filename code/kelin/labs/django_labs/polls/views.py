from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#     Create the following views:

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
    # discord = request.POST['discord']
    new_user = User.objects.create_user(username, password)
    new_user.save()
    return HttpResponse("You have registered")

def logoutUser(request):
    logout(request)
    return HttpResponse("you are not logged in")

def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if request.user is not None:
        login(request, user)
        return HttpResponse("You're logged in")
    else:
        return HttpResponse("Username and password does not match")