from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import MyImage
# Create your views here.
def index(request):
    imgs = MyImage.objects.all()
    return render(request, 'index.html', {'imgs': imgs})

def upload_picture(request):
    img = request.FILES.get('picture')
    title = request.POST['title']
    new_img = MyImage(title=title, img=img)
    new_img.save()
    return redirect('/')
