from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    return render(request, 'myapp/profile.html', {'user': request.user})

def sign_in(request):
    errors = []

    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            errors.append("Invalid login information!")

    return render(request, 'myapp/login.html', {'errors': errors})

def sign_out(request):
    logout(request)
    return redirect('/')

def register(request):
    errors = []

    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
            )
            
            login(request, user)
            return redirect('/')
        else:
            errors.append("Mismatching passwords!")
    
    return render(request, 'myapp/register.html', {'errors': errors})