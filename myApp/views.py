from .services import generate_request
from django.shortcuts import render,redirect
# Create your views here.

def indexView(request):


    return render(request,"app/index.html")

def loginView(request):

    return render(request,"app/login.html")

def peliculasView(request):

    return render(request,"app/peliculas.html")




