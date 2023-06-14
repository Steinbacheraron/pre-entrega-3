from django.shortcuts import render
from .models import Registrarse, Profesores, Alumnos
from .forms import Registrar, BuscoAlumnoForm, BuscoProfesorForm


def inicio(request):
    return render(request, "AppStein/inicio.html")


def alumnos(request):
    return render(request, "AppStein/alumnos.html")


def buscar_alumno(request):
    if request.method == 'POST':
        buscar_alumno = BuscoAlumnoForm(request.POST)
        if buscar_alumno.is_valid():
            info = buscar_alumno.cleaned_data
            alumnos = Alumnos.objects.filter(nombre__icontains=info["nombre"])
            return render(request, "AppStein/busca_alumno.html", {"Alumnos": alumnos})
    else:
        buscar_alumno = BuscoAlumnoForm()
        return render(request, "AppStein/busca_alumno.html", {"Alumno": buscar_alumno})


def profesores(request):
    return render(request, "AppStein/profesores.html")


def buscar_profesor(request):
    if request.method == 'POST':
        buscar_profesor = BuscoProfesorForm(request.POST)
        if buscar_profesor.is_valid():
            info = buscar_profesor.cleaned_data
            profesores = Profesores.objects.filter(nombre__icontains=info["nombre"])
            return render(request, "AppStein/busca_profe_api.html", {"Profesores": profesores})
    else:
        buscar_profesor = BuscoProfesorForm()
        return render(request, "AppStein/busca_profe_api.html", {"Profesor": buscar_profesor})


def registrarse(request):
    if request.method =='POST':
        mi_registro = Registrar(request.POST)
        
        if mi_registro.is_valid():
            informacion = mi_registro.cleaned_data
            curso = Registrarse(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], dni=request.POST['dni'])
            curso.save()
            return render(request, "AppStein/inicio.html")
    else: 
        mi_registro = Registrar()
        
    return render(request, "AppStein/registrarse.html")


    

        
        






















    