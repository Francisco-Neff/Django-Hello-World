from ast import For
from django.shortcuts import render
from .forms import FormularioWorld1Simple
from django.views.generic import View

# Create your views here.
def homepage_world2(request):
    #Página de inicio
    return render(request, 'index_world2.html')


def parametros_url(request,param):
    #respuesta por parametro en la URL
    context={'parametro':param}
    return render(request,'respuesta_url.html',context)

class param_Template(View):
    #Respuesta en los parametros en URL basado en Vistas.
    template_name = "class_template.html"
    form = FormularioWorld1Simple()

    def get(self, request,param,*args, **kwargs):
        form = FormularioWorld1Simple()
        respuesta = 'Has entrado por una petición HTTP ' +param
        context = {'form':form,'respuesta':respuesta}
        return render(request,self.template_name,context)

    def post(self, request,param,*args, **kwargs):
        
        form = FormularioWorld1Simple(request.POST)
        respuesta = 'Has enviado un formulario no valido y has creado petición HTTP ' +param
        if form.is_valid():
            respuesta = 'Has enviado "'+request.POST.get('campo1')+'" y creado una petición HTTP ' +param

        context = {'form':form,'respuesta':respuesta}
        return render(request,self.template_name,context)