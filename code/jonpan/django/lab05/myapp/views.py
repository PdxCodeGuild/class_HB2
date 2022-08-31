from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse 
from .models import BlogPost

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

@login_required
def user_profile(request):
    posts = BlogPost.objects.filter(user=request.user)

    context = {
        "posts": posts
    }

    return render(request, 'myapp/profile.html', context)

def view_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    context = {
        "blog": blog
    }
    return render(request, 'myapp/blogpost.html', context)

@login_required
def create(request):

    if request.method == 'GET':
        form = request.GET
        return render(request, 'myapp/create.html' )

    elif request.method == 'POST':

        form = request.POST
        title = form.get('title')
        body = form.get('body')        
        user = request.user      

        blog_post = BlogPost.objects.create(

            title=title,
            body=body,
            user=user,

        )
        print(blog_post.date_created, blog_post)

        return redirect(reverse('myapp:user_profile'))