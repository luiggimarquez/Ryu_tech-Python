from django.shortcuts import render
from django.http import HttpResponse
from .forms import EstudiantesForm, ProfesoresForm, CursosForm
from .models import Curso

def base(request):
    hero = True
    return render(request, 'index.html',{
        'hero': hero
    })
    

def signup(request):
    return render(request, "signUp.html")

def estudiantes(request):

    if(request.method == 'GET'):
   
        return render(request, "estudiantes.html", {
            'form' : EstudiantesForm 
        })
    
    else: 
        try:
            form = EstudiantesForm(request.POST)
            form.save()
        except:
            #Si hay dato publicado renderiza el form con el mensaje de error
            return render(request, "estudiantes.html", {
            'form' : EstudiantesForm, 'error': 'Correo/DNI ya registrado' 
        })
        #Si no hay error renderiza nuevamente el formulario normal
        return render(request, "estudiantes.html", {
            'form' : EstudiantesForm 
        })
    

def profesores(request):

    if(request.method == 'GET'):
        return render(request, "profesores.html",{
            'form': ProfesoresForm
        })
    else:
        try:
            form = ProfesoresForm(request.POST)
            form.save()
        except:
             #Si hay dato publicado renderiza el form con el mensaje de error
            return render(request, "profesores.html",{
            'form': ProfesoresForm, 'error': 'Correo/DNI ya registrado'
        })
        #Si no hay error renderiza nuevamente el formulario normal
        return render(request, "profesores.html",{
            'form': ProfesoresForm
        })


def cursos(request):

    if(request.method == 'GET'):
        return render(request, "cursos.html",{
            'form': CursosForm
        })
    else:

        """ try:
            form= CursosForm(request.POST)
            form.save()
        except:
            return render(request, "cursos.html",{
                'form': CursosForm, 'error': 'Correo/DNI ya registrado'
            }) """
        
        print(request.POST)
        form= CursosForm(request.POST )
        x = form.save(commit=False)
        x.save()
        form.save_m2m()

        return render(request, "cursos.html",{
                'form': CursosForm
            })

        
        return render(request, "cursos.html",{
            'form': CursosForm
        })

def busqueda(request):

    
    if(request.method == 'GET'):

        return render(request, 'busqueda.html')
        
    else:
        try:
            empty = False
            consulta = Curso.objects.filter(numero_cursada = request.POST['busqueda'])
            #print("Ejemplo", request.POST['busqueda'])
            """ for x in consulta:
                print (x.numero_cursada)
                print (x.curso)
                print(x.docente)
                for y in x.alumnos.all():
                    print(y)
            """
            if(len(consulta) == 0):
                empty = True

            return render(request, 'busqueda.html', {

                'consulta' : consulta, 'empty' : empty
            })
        except:
            return render(request, 'busqueda.html', {

                'error' : 'Se ha producido un error'
            })
