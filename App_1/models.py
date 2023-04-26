from django.db import models
from django import forms

# Create your models here.
class Estudiantes (models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    edad = models.IntegerField() 
    email = models.EmailField(max_length=100, unique=True)

    def __str__ (self):
        return f"{self.name} {self.lastname}"
    
    class Meta:
        verbose_name_plural = "Estudiantes"


class Profesores (models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    email= models.EmailField(max_length=100, unique=True)
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name_plural = "Profesores" 
    

class Curso (models.Model):
   
    curso = models.CharField(max_length=100)
    numero_cursada = models.IntegerField(unique=True)
    docente = models.ForeignKey(Profesores, null=True, blank=True, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Estudiantes, blank=True)
    
    def __str__(self):
        return f"{self.curso}"
    
    class Meta:
        verbose_name_plural = "Cursos"