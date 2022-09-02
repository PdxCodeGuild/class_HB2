import random
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request, 'temp/hotorcold.html', {'temperature': random.randint(50, 100)})