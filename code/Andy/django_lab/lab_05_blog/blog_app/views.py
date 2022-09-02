from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse 
from .models import BlogPost
from django.contrib.auth.models import User
# from django.contrib.auth import models # models.User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
# from django.urls import reverse 

def index(request):
    posts = BlogPost.objects.all()
    context={
        'posts': posts,
    }
    return render(request, 'blog_app/index.html', context)