from django.urls import path
from . import views

urlpatterns = [
    path("", views.base),
    path("signup/", views.signup, name="signup"),
    path("estudiantes/", views.estudiantes, name= "estudiantes"),
    path("profesores/", views.profesores, name = "profesores"),
    path("cursos/", views.cursos, name = "cursos"),
    path("busqueda/", views.busqueda, name= "busqueda")
]