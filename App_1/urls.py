from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="home"),
    path("signup/", views.signup, name="signup"),
    path("estudiantes/", views.estudiantes, name= "estudiantes"),
    path("profesores/", views.profesores, name = "profesores"),
    path("cursos/", views.cursos, name = "cursos"),
    path("busqueda/", views.busqueda, name= "busqueda"),
    path("logout/", views.log_out, name= "logout"),
    path("login/", views.log_in , name = "login")
]