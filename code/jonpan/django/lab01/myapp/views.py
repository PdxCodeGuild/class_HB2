from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel, MyModel2

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    print(request.POST)
    return HttpResponse('form received')

# Create your views here.
