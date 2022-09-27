from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import CreateBlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required
def index_view(request):
    the_query_set = CreateBlogPost.objects.all()
    context = {
        'posts': the_query_set,
        'user': request.user
    }

    return render(request, 'blog_app/index.html', context)

@login_required
def profile_view(request, username):
    the_user = get_object_or_404(User, username=username)
    print(type(the_user))
    the_query_set = CreateBlogPost.objects.filter(user=the_user)
    context = {
        'posts': the_query_set,
        }

    return render(request, 'blog_app/profile.html', context)




def logout_view(request):
    logout(request)
    return redirect('blog_app:login_view')






def register_view(request):
    # request_method = request.method
    # print("request_method", request_method)
    if request.method == "POST":
        print("POST REQUEST")
        print("request.POST.keys",request.POST.keys)
        # <built-in method keys of QueryDict object at 0x7f2d674c23b0>
        print("request.POST.keys",request.POST.keys())
        # dict_keys(['csrfmiddlewaretoken', 'username', 'password', 'discord'])
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        new_user = User.objects.create_user(username=username, password=password, email=email)
        login(request, new_user)
        return render(request, 'blog_app/index.html')
        print("new_user:", new_user)
    else:
        return render(request, 'blog_app/register.html')
    

    
    # user = User.objects.create_user(username, email=None, password=None)
    

# http://127.0.0.1:8000/blog-app/register-page/register
# http://127.0.0.1:8000/blog-app/register-page/blog-app/register

def login_view(request):
    # request_method = request.method
    # print("request_method", request_method)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            # return redirect("/")
            print (user.username)
            print (reverse('blog_app:profile_view', kwargs={'username': user.username}))
            # print (redirect('blog_app:profile_view', username=user.username))
            # print (reverse('blog_app:profile_view', {'username': user.username}))
            return HttpResponseRedirect(
                reverse('blog_app:profile_view', kwargs={'username': user.username})
                )
           
        else:
            return render(request, 'blog_app/login.html')
        #    return HttpResponse(user)
           
    else:
        # return HttpResponse(request.user)
        return render(request, 'blog_app/login.html')


def create_view(request):
    print(request.POST)
    post_title = request.POST['title']
    post_body = request.POST['body']
    post_user = request.user
    # print('title: post_title, )
    print("request.POST.keys",request.POST.keys())
    new_post = CreateBlogPost.objects.create(title=post_title, body=post_body, user=post_user)
    print(new_post, new_post.id)
            
    return redirect("/")
    




# def login
# https://docs.djangoproject.com/en/4.1/topics/auth/default/#auth-admin


# @login_required






