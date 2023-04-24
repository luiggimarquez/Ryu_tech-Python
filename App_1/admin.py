from django.contrib import admin


# Register your models here.
from .models import Estudiantes, Curso, Profesores

admin.site.register(Estudiantes)
admin.site.register(Curso)
admin.site.register(Profesores)
