from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render
from .forms import FormularioWorld1Simple
# Create your views here.


def homepage_world1(request):
    #Página de inicio
    return render(request, 'index_world1.html')


def model(request):
    #Se indica como usar models de Django.
    return render(request, 'model.html')

def formsimple(request):
   #Definición de un formulario simple.
    if request.method == 'POST':
        form = FormularioWorld1Simple(request.POST)    
        if form.is_valid():
            respuesta = 'He recibido "' + form.cleaned_data.get('campo1') + '" por tu parte'
            form=FormularioWorld1Simple()
    else:
        respuesta = 'Ingresa un valor para recibir una respuesta del formulario'
        form = FormularioWorld1Simple()
       
    context = {'form':form,'respuesta':respuesta}
    return render(request, 'form.html',context)