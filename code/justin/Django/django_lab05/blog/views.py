from urllib import request
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You registered! gj well played.")
            return redirect('main:homepage')
    form = NewUserForm
    context = {
        'form':form
    }
    return render(request,'blog/register.html', context )

def login(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages = messages.info(f'you are logged in as {username}')
                return redirect('blog:profile')
            else:
                messages = messages.error('invalide somethign or another')
        else:
            messages = messages.error('somethings wrong i can feel it')
    form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form':form})

def profile(request):
    context = {
        'message': 'this is the profile page'
    }
    return render(request, 'blog/profile.html', context)
    pass
