from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hola(request):
    return HttpResponse('Hola')