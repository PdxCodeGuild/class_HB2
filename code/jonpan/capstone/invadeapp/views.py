from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from .models import Champions
from django.core.paginator import Paginator
from django.core import serializers
from rest_framework import status
from rest_framework.response import Response

def index(request):
    return render(request, 'invadeapp/index.html')

def champions(request):
    champion = list(Champions.objects.all().values())
    return JsonResponse(champion,
        safe=False, status=status.HTTP_200_OK)