from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myview(request):
    return HttpResponse('hello world! Youre at the todo index.')