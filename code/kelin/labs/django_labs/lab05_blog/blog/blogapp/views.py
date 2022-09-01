from datetime import datetime
from .forms import NewUser
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.forms import AuthenticationForm
from .models import BlogPost
from .forms import BlogPost

# Create the following views:

# Register /register/
# form for creating a new user
# redirect to /profile/ after registering

def register(request):
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('blog:profile')
        else:
            return redirect('blog:register')
    form = NewUser()
    context = {
        'form':form,
    }

    return render(request, 'blog/register.html')

# Login /login/
# form for logging a user in
# redirect to /profile/ after logging in
        
def login(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if user is not None:
                return redirect('blog:profile')
            else:
                return redirect('blog:login')
        else:
            return redirect('blog:login')
    form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form':form})

# Profile /profile/
# a protected page only logged in users can see
# just show a welcome message for now

def profile(request):
    blog = BlogPost.objects.filter(user=request.user).all()
    context = {
        'message': 'Profile page',
        'blog':blog,
    }
    return render(request, 'blog/profile.html', context)
    pass

def logout_view(request):
    logout(request)
    return redirect('blog:login')


def create(request):
    if User.is_authenticated:
        if request.method == 'POST':
            form = BlogPost(request.POST, request.FILES)            
            if form.is_valid():
                form.save()
                return redirect('blog:profile')
            else:
                pass
        else:
            person = get_user(request)
            print('Loading user')
            form = BlogPost(initial={'user':person})        

        context = {
            'form':form
        }
        return render(request, 'blog/create.html', context)
    else:
        return redirect('blog:login')
