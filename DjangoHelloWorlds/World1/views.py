from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render
from .forms import FormularioWorld1Simple, FormularioModel
from .models import Modelo1
# Create your views here.


def homepage_world1(request):
    #Página de inicio
    return render(request, 'index_world1.html')


def model(request):
    #Se indica como usar models de Django.
    return render(request, 'model.html')

def forms_simple(request):
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


def forms_model(request):
    #Definición de un formulario a través de Model.
    if request.method == 'POST':
        form = FormularioModel(request.POST)
        if form.is_valid():
            respuesta = 'He recibido "' + form.cleaned_data.get('campo1') +' y '+ form.cleaned_data.get('campo2')  + '" por tu parte'
    else:
        respuesta = 'Ingresa un valor para recibir una respuesta del formulario'
        form = FormularioModel()
       
    context = {'form':form,'respuesta':respuesta}
    return render(request, 'form_model.html',context)     


def datos_model(request):
    #Definición de como guardar y mostrar los datos del último registro.
    if request.method == 'POST':
        form = FormularioModel(request.POST)
        if form.is_valid():
            modelo = Modelo1(campo1=form.cleaned_data.get('campo1'),campo2=form.cleaned_data.get('campo2'))
            modelo.save()
            registro = Modelo1.objects.latest('id')
            getattr(registro,'campo1')
            respuesta = 'Tu modelo tiene ahora los datos:' + getattr(registro,'campo1') + ' y ' + getattr(registro,'campo2')
    else:
        respuesta = 'Ingresa un valor para recibir una respuesta del formulario'
        form = FormularioModel()
       
    context = {'form':form,'respuesta':respuesta}
    return render(request, 'datos_model.html',context) 