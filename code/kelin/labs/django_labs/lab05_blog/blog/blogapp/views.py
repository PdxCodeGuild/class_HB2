from datetime import datetime
from .forms import 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from .models import BlogPost

# Create the following views:

# Register /register/
# form for creating a new user
# redirect to /profile/ after registering

from .forms import SignUpForm
 
def register(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    
# Login /login/
# form for logging a user in
# redirect to /profile/ after logging in
    
def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if request.user is not None:
        login(request, user)
        return HTTPResponse("Logged in")
    else:
        return HTTPResponse(user)

# Profile /profile/
# a protected page only logged in users can see
# just show a welcome message for now

@login_required
def profile(request):
    username = username
    userposts = userposts
    return render(request, '/profile/profile.html')

def newpost(request):
    title = BlogPost.title
    body = request.POST['body']
    date = datetime
    return render(request, '/blogpost/blogpost.html')