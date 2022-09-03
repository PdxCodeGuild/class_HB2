from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CreateBlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# def profile_view(request):
#     the_query_set = 'Goodbuy, World! Enjoy the sale!'
#     return HttpResponse(the_query_set)




def index_view(request):
    the_query_set = CreateBlogPost.objects.all()
    context = {
        'posts': the_query_set
    }
    return render(request, 'blog_app/index.html', context)


def register_view(request):
    request_method = request.method
    print("request_method", request_method)
    if request_method == "POST":
        print("POST REQUEST")
        print("request.POST.keys",request.POST.keys)
        # <built-in method keys of QueryDict object at 0x7f2d674c23b0>
        print("request.POST.keys",request.POST.keys())
        # dict_keys(['csrfmiddlewaretoken', 'username', 'password', 'discord'])
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        new_user = User.objects.create_user(username, password, email)
        return HttpResponse("You have registered")
        print("new_user:", new_user)
        return render(request, 'blog_app/register.html')
    else:
        return render(request, 'blog_app/register.html')
    

    
    # user = User.objects.create_user(username, email=None, password=None)
    

# http://127.0.0.1:8000/blog-app/register-page/register
# http://127.0.0.1:8000/blog-app/register-page/blog-app/register

def login_view(request):
    return render(request, 'blog_app/login.html')


def create_view(request):
    if request.method == "POST":
        post_title = request.POST['title']
        post_body = request.POST['body']
        print("request.POST.keys",request.POST.keys())
        new_post = CreateBlogPost(title=post_title, body=post_body)
        new_post.save()
    # return render(request, 'blog_app/create.html')
    

    return redirect("/")



# def login
# https://docs.djangoproject.com/en/4.1/topics/auth/default/#auth-admin


# @login_required






