from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponse

def profile(response):
    return render(response, "blogapp/profile.html")

def register(response):
    if response.method == 'POST':
       form = RegistrationForm(response.POST)  
       if form.is_valid():
            form.save()
       return redirect('profile/')
    else:
        form = RegistrationForm()
    return render(response, 'blogapp/register.html', {'form':form})
# Create your views here.
