from django.forms import ModelForm
from .models import Estudiantes, Profesores, Curso
from django import forms


class EstudiantesForm(ModelForm):
    class Meta:
        model = Estudiantes
        fields =['name','lastname', 'dni', 'edad', 'email']

class ProfesoresForm(ModelForm):
    class Meta:
        model = Profesores
        fields = ['name','lastname', 'dni','email','profesion' ]

class CursosForm(ModelForm):
    alumnos = forms.ModelMultipleChoiceField(
                        queryset=Estudiantes.objects.all().order_by('name'),
                        widget=forms.CheckboxSelectMultiple,required=False)
    class Meta:
        model = Curso
        fields = ['curso','numero_cursada', 'docente','alumnos']


