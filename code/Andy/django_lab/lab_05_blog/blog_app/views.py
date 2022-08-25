from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost



def register(request):
    print(request.POST)

    username = request.POST['username']

    return HttpResponse(f'Welcome {username}?')

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

