from django import forms

class Registrar(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    dni = forms.IntegerField()
      
class BuscoAlumnoForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    
class BuscoProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    materia = forms.CharField()
    
