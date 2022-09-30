from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon
from django.core.paginator import Paginator

def index(request):
    return render(request, 'pokeapp/index.html')

def pokemon(request):
    pokemon = Pokemon.objects.all()
    data_to_return = pokemon.values("number", "name", "image_front")
    paginator = Paginator(data_to_return, 20)
    page_number = request.GET.get('page')
    print(paginator.num_pages)
    data = list(paginator.get_page(page_number))
    data.append(paginator.num_pages)
    return JsonResponse({"data": data}, safe=False)
    # print("hello")