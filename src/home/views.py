from django.shortcuts import render , redirect
from .views import *


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request , "home/home.html" , {})


