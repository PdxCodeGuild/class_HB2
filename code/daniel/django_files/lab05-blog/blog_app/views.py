from django.http import HttpResponse
from django.shortcuts import render
from .models import CreateBlogPost

# def profile_view(request):
#     the_query_set = 'Goodbuy, World! Enjoy the sale!'
#     return HttpResponse(the_query_set)

def profile_view(request):
    the_query_set = CreateBlogPost.objects.all()
    context = {
        'posts': the_query_set
    }
    
    return render(request, 'blog_app/profile_template.html', context)




