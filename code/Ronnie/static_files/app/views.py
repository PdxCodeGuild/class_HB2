from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render

def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'app/index.html', context)