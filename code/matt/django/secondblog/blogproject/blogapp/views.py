from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html', {})

# Create your views here.
