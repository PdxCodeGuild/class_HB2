from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    return(request)

def sign_in(request):
    errors = []

    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password'],
        
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            errors.append("Invalid login information")

    return render(request,'accounts', 'myapp/login.html', {'errors:'})

def sign_out(request):
    logout(request)
    return redirect('/')

# def register(request):

#     if request.method == 'GET':
#         context = {
#             'message': 'Please register your account.'
#         }
#         return render(request, 'myapp/register.html', context)

#     elif request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         new_user = User.objects.create_user(username, password)
#         new_user.save()
#         return HttpResponseRedirect(reverse('myapp:profile'))

# def login_user(request):
#     if request.method == 'GET':
#         return render(request, 'myapp/login.html')

#     elif request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if request.user is not None:
#             login(request, user)
#             print(user)
#             return HttpResponse(user)
#        else:
#             print(user)
#             return HttpResponse(user)

# def index(request):
#     context = {
#         'message': 'Welcome to the homepage.'
#     }
#     return render(request, 'myapp/index.html', context)

# def login_user(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)       
#         return HttpResponse('You are logged in')
#     else:
#         return HttpResponse('Please try logging in again')