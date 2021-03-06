"""DjangoHelloWorlds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from World1 import views as world1
from World2 import views as world2

urlpatterns = [
    
    path('', views.homepage ,name='inicio' ),
    path('holamundo', views.holamundo ,name='holamundo' ),
    path('primerospasos', views.primerospasos ,name='primerospasos' ),
    path('plantillas', views.plantillas ,name='plantillas' ),
    path('app', views.app_servicios ,name='app' ),
    
    
    #World1
    
    path('world1',  world1.homepage_world1   ,name='world1' ),
    path('model', world1.model ,name='model' ),
    path('formsimple', world1.forms_simple  ,name='formulario_simple' ),
    path('formsmodel', world1.forms_model ,name='formulario_model' ),
    path('datosmodel', world1.datos_model ,name='datosmodel' ),

    #World2
    path('world2',  world2.homepage_world2   ,name='world2' ),
    path('param/<str:param>',  world2.parametros_url  , name='param' ),
    path('class/<str:param>',  world2.param_Template.as_view()  , name='class' ),

    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
