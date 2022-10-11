from django.shortcuts import render
from .models import Pokemon
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse   

# Create your views here.
def pokemon(request):
    pokemon = Pokemon.objects.all()
    ret = []
    
    # for p in pokemon:
    #     number = p.number
    #     name = p.name
    #     image_front = p.image_front
    #     image_back = p.image_back
    #     ret.append({'number': number, 'name': name, 'image_front': image_front, 'image_back': image_back})

    # # return JsonResponse(request, 'index.html', {'pokemon':pokemon})
    return JsonResponse(pokemon, safe=False)
    # return JsonResponse(ret, safe=False)

    # data = serializers.serialize('json', 
    #                              Pokemon.objects.all(), 
    #                              fields=('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type_info', 'id'))
    # return HttpResponse(data, content_type='application/json')
