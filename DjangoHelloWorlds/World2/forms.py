from django import forms

#Crear Formularios

#Formulario Simple
class FormularioWorld1Simple(forms.Form):
    campo1 = forms.CharField(label='campo1', max_length=100)
