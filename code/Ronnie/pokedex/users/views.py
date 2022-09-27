from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("accounts:profile")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserCreationForm()
	return render (request=request, template_name="registration/register.html", context={"form":form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})