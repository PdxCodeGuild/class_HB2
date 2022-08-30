from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse 
from .models import BlogPost
from django.contrib.auth.models import User
# from django.contrib.auth import models # models.User
from django.contrib.auth import login
# from django.urls import reverse 

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

def register(request):

    # print('print request: ', request)
    # # print('print request: ', dir(request))
    # print('print request.POST: ', request.POST)
    # print('print request.POST.keys: ', request.POST.keys())
    form = request.POST
    # print('form string', form)
    # form string <QueryDict: {
    # 'csrfmiddlewaretoken': ['ejRwnxL68LDDQ2iDieoTuhkZLNy5Rp7nx1o3zp9i3vLx5iRdzhuCgIM9Gv0u5Zf1'],
    # 'username': ['andy'],
    # 'password': ['345']
    # }>
    the_username = form['username']
    the_password = form['password']
    # print(the_username, the_password)
    # print(dir(User.objects))
    new_user = User.objects.create_user(the_username, the_password)
    login(request, user=new_user)
    # test_user = User(username='bunbun')
    # test_user.save()
    return HttpResponseRedirect(reverse('blog_app:profile'))

