from dataclasses import fields
from django import forms
from World1.models import Modelo1

#Crear Formularios

#Formulario Simple
class FormularioWorld1Simple(forms.Form):
    campo1 = forms.CharField(label='campo1', max_length=100)


#Formulario basado en Model
class FormularioModel(forms.ModelForm):
    class Meta:
        model = Modelo1
        fields = ['campo1','campo2']