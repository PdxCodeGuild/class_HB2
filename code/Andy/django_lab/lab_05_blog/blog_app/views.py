from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import login


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

