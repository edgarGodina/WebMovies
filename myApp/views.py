from .services import generate_request
from django.shortcuts import render,redirect
# Create your views here.

def indexView(request):


    return render(request,"app/index.html")




