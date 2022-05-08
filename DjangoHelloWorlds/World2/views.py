from ast import For
from django.shortcuts import render
from .forms import FormularioWorld1Simple

# Create your views here.
def homepage_world2(request):
    #Página de inicio
    return render(request, 'index_world2.html')


def parametros_url(request,param):
    #respuesta por parametro en la URL
    context={'parametro':param}
    return render(request,'respuesta_url.html',context)