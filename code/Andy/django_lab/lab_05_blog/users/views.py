from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from blog_app.models import BlogPost


# Create your views here.
def login(request):
    """
    this just renders the signup page 
    """
    if request.method == 'GET':

        return render(request, 'blog_app/login.html')

    else:
        request_dict = request.POST

        print('request dictionary:', request_dict)
        # request dictionary: <QueryDict: {'csrfmiddlewaretoken': ['Q1fDtEc5K7vG1ZWqPpjVzDTB3m5VoHiBok0a6kMXDtPUASEtGzEwbnBnLaSCIXcj'], 'username': ['rob']}>
        print('keys:', request_dict.keys())
        # keys: dict_keys(['csrfmiddlewaretoken', 'username'])
        the_username = request_dict['username']
        the_password = request_dict['password']
        authenticated_user = authenticate(request, username=the_username, password=the_password)
        # print('authenticated user', authenticated_user) 
        # print('authenticated user type', type(authenticated_user))
        # print("user:", the_username)
        return redirect(reverse('blog_app:index'))


@login_required
def profile(request, username):
    user = get_object_or_404(User,username=username)

    blog_posts = BlogPost.objects.filter(user=user)
    # blog_posts = 'post from database'
    context ={
        'posts': blog_posts,
    }

    return render(request, 'blog_app/profile.html', context )

def logout_user(request):
     logout(request)
     return redirect('blog_app:login.html')

def register(request):
    if request.method == 'GET':

        return render(request, 'blog_app/signup.html')
    

    # print('print request: ', request)
    # # print('print request: ', dir(request))
    # print('print request.POST: ', request.POST)
    # print('print request.POST.keys: ', request.POST.keys())
    elif request.method == 'POST':
        
        form = request.POST
        # print('form string', form)
        # form string <QueryDict: {
        # 'csrfmiddlewaretoken': ['ejRwnxL68LDDQ2iDieoTuhkZLNy5Rp7nx1o3zp9i3vLx5iRdzhuCgIM9Gv0u5Zf1'],
        # 'username': ['andy'],
        # 'password': ['345']
        # }>
        the_username = form.get('username')
        the_password = form.get('password')
        print(the_username, the_password)
        # print(dir(User.objects))
        user = User.objects.create_user(username=the_username,password=the_password)
        
        if user is not None:
            login(request, user)
        # test_user = User(username='bunbun')
        # test_user.save()
        return redirect(reverse('users:profile', kwargs={'username':request.user.username}))

