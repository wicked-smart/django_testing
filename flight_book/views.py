from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("What's up man! how's life going ..having fun doing this software developement thing!!!")
