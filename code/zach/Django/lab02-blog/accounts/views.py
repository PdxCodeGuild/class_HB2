from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/register.html'

@login_required
def profile_view(request):
    return render(request, 'profile.html')