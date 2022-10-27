from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import MyModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("NuggetServer:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	else:
		form = NewUserForm()
	return render(request, template_name="NuggetServer/register.html", context={"register_form":form})

    




@login_required
def myhomepage(request):
    return render(request, "NuggetServer/index.html")

# def myflash(request):
#     print("flash")

# def mydatabase(request):
#     print("database")


def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'NuggetServer/mytemplate.html', context)

def mycreate(request):
    myfield = request.POST['myfield']
    mymodel = MyModel(myfield=myfield)
    mymodel.save()
    return HttpResponseRedirect(reverse('NuggetServer:myview'))