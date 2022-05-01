from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from pathlib import Path

def homepage(request):
    #Pagina de inicio
    return render(request, 'index.html')