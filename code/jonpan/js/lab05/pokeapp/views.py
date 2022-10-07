from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from .models import Pokemon
from django.core.paginator import Paginator
from django.core import serializers
from rest_framework import status
from rest_framework.response import Response

def index(request):
    return render(request, 'pokeapp/index.html')

def pokemon(request):
    pokemon = list(Pokemon.objects.all().values())
    return JsonResponse(pokemon,
        safe=False, status=status.HTTP_200_OK)
    # pokemon = Pokemon.objects.all()
    # data = serializers.serialize("json",pokemon)
    # context = {"data":data}
    # return JsonResponse(data, safe=False)
    # return HttpResponse(data, content_type="application/json")

# def getPokemon(request):
#     pokemon = get_object_or_404(name=name)
#     return JsonResponse(pokemon,
#         safe=False, status=status.HTTP_200_OK)

# build form in html, not forms.py, tie action to name of the fuction
    










    # return render(request, 'pokeapp/index.html', {'pokemon':pokemon})
    # pokemon = Pokemon.objects.all()
    # data_to_return = pokemon.values("number", "name", "image_front")
    # paginator = Paginator(data_to_return, 20)
    # page_number = request.GET.get('page')
    # print(paginator.num_pages)
    # data = list(paginator.get_page(page_number))
    # data.append(paginator.num_pages)
    # return JsonResponse({"data": data}, safe=False)
    # print("hello")


# above works, pull into vue application with an API call, axios