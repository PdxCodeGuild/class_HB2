from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        form =  NewUserForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            user = authenticate(username=username, password=raw_password, email=email)
            form.save()
            login(request, user)

            return redirect('index')
    else:
        form = NewUserForm()
    return render(request, 'registration/register.html', {'form': form})