from urllib import request
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import BlogPost
from .forms import BlogForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('blog:profile')
        else:
            return redirect('blog:register')    
    form = NewUserForm()
    context = {
        'form':form,
    }

    return render(request,'blog/register.html', context )

def logins(request):
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

def profile(request):
    # form = BlogForm()
    blog = BlogPost.objects.filter(user=request.user).all()
    context = {
        'message': 'this is the profile page',
        'blog':blog,
        # 'form':form,
    }
    return render(request, 'blog/profile.html', context)
    pass

def logout_view(request):
    logout(request)
    return redirect('blog:login')

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:profile')
        else:
            pass
    else:
        pass
    form = BlogForm()

    context = {
        'form':form
    }
    return render(request, 'blog/create.html', context)
