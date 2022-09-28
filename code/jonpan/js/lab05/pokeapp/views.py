from django.http import HttpResponse

def myview(request):
    return HttpResponse('hello world!')


# def pokemon(request):
