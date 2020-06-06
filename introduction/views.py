from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def show_introduction(request):
    return render(request, 'introduction/intro.html')