from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #Página de inicio
    return render(request, 'index.html')

def holamundo(request):
    #Se indica como se crea un nuevo proyecto y realizar nuestro primer Hola mundo.
    return render(request, 'holamundo.html')

def primerospasos(request):
    #Se indica como se crea el directorio de templates y archivos estáticos e incluir una página de inicio.
    return render(request, 'primerospasos.html')

def plantillas(request):
    #Se indica como crear y usar una plantilla.
    return render(request, 'plantillas.html')
    
def app_servicios(request):
    #Se indica como crear una nueva app.
    return render(request, 'app_servicios.html')

def clase_model(request):
    #Se indica como usar models y los forms de Django.
    return render(request, 'modelform.html')
