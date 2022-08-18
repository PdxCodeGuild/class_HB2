from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request ----> resoibse
# reqyest handler
# action

def say_hello(request):
    return HttpResponse('hello world')