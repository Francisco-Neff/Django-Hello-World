from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from pathlib import Path

def homepage(request):
    #Pagina de inicio
    return render(request, 'index.html')

def holamundo(request):
    #Se indica como se crea un nuevo proyecto y realizar nuestro primer Hola mundo.
    return render(request, 'holamundo.html')

def primerospasos(request):
    #Se indica como se crea el directorio de templates y archivos estaticos e incluir una página de inicio.
    return render(request, 'primerospasos.html')

def plantillas(request):
    return render(request, 'index.html')