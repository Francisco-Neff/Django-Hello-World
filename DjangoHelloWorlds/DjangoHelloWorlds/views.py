from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from pathlib import Path

def homepage(request):
    #Pagina de inicio
    return render(request, 'index.html')

def holamundo(request):
    #Se indica como se crea un nuevo proyecyo y crear una pagina de inicio.
    return render(request, 'index.html')