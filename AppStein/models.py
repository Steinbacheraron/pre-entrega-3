from django.db import models

# Create your models here.

class Inicio(models.Model):
    def __str__(self):
        return f"¡Bienvenidos!"
    
class Registrarse(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    dni = models.IntegerField()
    
    def __str__(self):
             return f"Fuiste registrado con éxito: {self.nombre}"
         

class Alumnos(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    dni = models.IntegerField()
    
    

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    dni = models.IntegerField()
