from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog_app.models import BlogPost
from django.contrib.auth import get_user

# Create your views here.
@login_required
def profile_view(request):
    user = get_user(request)
    blogs = BlogPost.objects.filter(user=user)
    context = {
        'blogs': blogs,
        'user': request.user
    }
    return render(request, 'profile.html', context)

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:profile')

#class UserProfileView(DetailView):
#    model = User
#    template_name = 'profile.html'
#    context_object_name = 'user_profile'
    
#    def get_object(self):
#        return get_object_or_404(User, username=self.kwargs['username'])