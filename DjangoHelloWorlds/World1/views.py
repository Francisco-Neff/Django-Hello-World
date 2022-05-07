from django.shortcuts import render

# Create your views here.


def homepage_world1(request):
    #Página de inicio
    return render(request, 'index_world1.html')


def model(request):
    #Se indica como usar models de Django.
    return render(request, 'model.html')
