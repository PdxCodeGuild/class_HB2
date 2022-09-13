from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogForm, UpdateForm
from django.urls import reverse_lazy

#We pull our forms from '''.forms''' and put them into our views for us to connect
#Creating ProfileView, ArticleView, CreatePostView, etc... for the ease of a view

class ProfileView(ListView):
    model = BlogPost 
    template_name = 'profile.html'
    ordering = ['-date_created',]

class ArticleView(DetailView):
    model = BlogPost 
    template_name = 'article.html'
    

#Telling it to use our BlogPost model AND BlogForm for styling
class CreatePostView(CreateView):
    model = BlogPost 
    #Because of this '''BlogForm''', we do not need to add any fields because they are already inside are forms.py
    form_class = BlogForm
    template_name = 'create.html'
   
class UpdatePostView(UpdateView):
    model = BlogPost 
    template_name = 'update.html'
    form_class = UpdateForm

class DeletePostView(DeleteView):
    model = BlogPost 
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

