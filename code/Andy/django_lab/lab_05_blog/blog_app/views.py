from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse 
from .models import BlogPost
from django.contrib.auth.models import User
# from django.contrib.auth import models # models.User
from django.contrib.auth import login, logout, authenticate, get_user
from django.contrib.auth.decorators import login_required 
# from django.urls import reverse
from blog_app.form import BlogForm 

def index(request):
    posts = BlogPost.objects.all()
    context={
        'posts': posts,
    }
    return render(request, 'blog_app/index.html', context)

def create(request):
    print('request', request)
    reg_user = get_user(request)
    # if User.is_authenticated:
    if request.method == 'POST':
        # print('request post', request.POST)
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
        # form = BlogForm()
        # form = BlogForm(initial = {'user':reg_user})

        # return HttpResponseRedirect(reverse('blog_app:create'),{'form_template': form})
        return redirect('users:profile', reg_user.username)
            
    else:
        form = BlogForm()
        print('reg_user', reg_user)
        print('reg_user', type(reg_user))
        form = BlogForm(initial = {'user':reg_user})


    
    
    return render(request, 'blog_app/create.html', {'form_template': form} )
    # return HttpResponseRedirect(reverse('blog_app:create'),{'form_template': form})