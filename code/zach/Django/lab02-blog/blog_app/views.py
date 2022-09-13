from django.shortcuts import render
from .models import BlogPost
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user

# Create your views here.
def create_post(request):
    title = request.POST['title']
    body = request.POST['body']
    user = get_user(request)
    BlogPost.objects.create(user=user, title=title, body=body)
    return HttpResponseRedirect(reverse('accounts:profile'))