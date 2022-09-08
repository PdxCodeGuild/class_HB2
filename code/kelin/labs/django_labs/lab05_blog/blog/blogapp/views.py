from django.contrib.auth.models import User
from django.shortcuts import  render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout, get_user
from django.contrib.auth.forms import AuthenticationForm
from .models import BlogPost
from .forms import BlogForm

# Create the following views:

# Register /register/
# form for creating a new user
# redirect to /profile/ after registering

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('blogapp:profile')
        else:
            return redirect('blogapp:register')    
    form = NewUserForm()
    context = {
        'form':form,
    }

    return render(request,'blog/register.html', context )

# Login /login/
# form for logging a user in
# redirect to /profile/ after logging in
        
def loginto(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if user is not None:
                return redirect('blogapp:profile')
            else:
                return redirect('blogapp:login')
        else:
            return redirect('blogapp:login')
    form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form':form})

# Profile /profile/
# a protected page only logged in users can see
# just show a welcome message for now

def profile(request):
    """Profile /profile/ a protected page only logged in users can see"""
    blog = BlogPost.objects.filter(user=request.user).all()
    context = {
        'message': 'Profile page',
        'blog':blog,
    }
    return render(request, 'blog/profile.html', context)
    pass

def logout_view(request):
    logout(request)
    return redirect('blogapp:login')


def create(request):
    if User.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)            
            if form.is_valid():
                form.save()
                return redirect('blogapp:profile')
            else:
                pass
        else:
            person = get_user(request)
            print('Loading user')
            form = BlogForm(initial={'user':person})        

        context = {
            'form':form
        }
        return render(request, 'blog/create.html', context)
    else:
        return redirect('blogapp:login')

# Allow users to edit their BlogPosts by creating an edit page. 
# Make sure you prevent users from editing eachother's blog posts (make sure the id for the blog post passed in via the path corresponds to a BlogPost for the logged-in User).
# Edit Post /edit/<int:blogpost_id>/
# form for editing an existing post

def edit(request, pk):
    template = 'blog/editpost.html'
    post = get_object_or_404(BlogPost, pk=pk)
    if User.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST, instance=post)
       
            if form.is_valid():
                form.save()
                messages.success(request, 'Blog Post Updated')
            else:
                pass
        else:
            form = BlogForm(instance=post)      

        context = {
            'form': form,
            'post': post,
        }
        return render(request, template, context)
    else:
        return redirect('blogapp:login')
