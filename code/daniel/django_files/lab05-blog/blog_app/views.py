from django.http import HttpResponse
from django.shortcuts import render
from .models import CreateBlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# def profile_view(request):
#     the_query_set = 'Goodbuy, World! Enjoy the sale!'
#     return HttpResponse(the_query_set)




def profile_view(request):
    the_query_set = CreateBlogPost.objects.all()
    context = {
        'posts': the_query_set
    }
    
    return render(request, 'blog_app/profile_template.html', context)


def register_view(request):

    # user = User.objects.create_user(username, email=None, password=None)
    return HttpResponse('register')


def login_view(request):
    return HttpResponse('login')





# def login
# https://docs.djangoproject.com/en/4.1/topics/auth/default/#auth-admin


# @login_required






