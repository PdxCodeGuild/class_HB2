from re import T
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
            errors.append("Invalid login information")
    
    return render(request, 'accounts/login.html', {'errors': errors})

def sign_out(request):
    logout(request)
    return redirect('/')