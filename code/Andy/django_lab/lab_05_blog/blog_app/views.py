from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import login

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
    
    return render(request, 'blog_app/register.html', {'errors': errors})

def signup(request):
    """
    this just renders the signup page 
    """
    return render(request, 'blog_app/signup.html')

def profile(request):
    blog_posts = BlogPost.objects.all()
    # blog_posts = 'post from database'
    context ={
        'posts': blog_posts
    }

    return render(request, 'blog_app/profile.html', context )

