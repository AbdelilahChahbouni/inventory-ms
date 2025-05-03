from django.shortcuts import render
from .views import *


def home(request):
    return render(request , "home/home.html" , {})


