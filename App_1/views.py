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
        
        form = EstudiantesForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, "estudiantes.html", {
                'form' : EstudiantesForm, 'saved': 'Datos almacenados correctamente' 
            })

        else:
            return render(request, "estudiantes.html", {
                'form' : EstudiantesForm, 'errors': form.errors 
            })

        """ except:
            #Si hay dato publicado renderiza el form con el mensaje de error
            return render(request, "estudiantes.html", {
            'form' : EstudiantesForm, 'error': 'Correo/DNI ya registrado' 
        })
        #Si no hay error renderiza nuevamente el formulario normal
        return render(request, "estudiantes.html", {
            'form' : EstudiantesForm 
        }) """
    

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

        form= CursosForm(request.POST ) 
        if (form.is_valid()):
  
            x = form.save(commit=False)
            x.save()
            form.save_m2m()

            return render(request, "cursos.html",{
                'form': CursosForm, 'saved': "Datos almacenados correctamente"
            })
        else:
            print('invalido')
            return render(request, "cursos.html",{
                'form': CursosForm, 'errors': form.errors
            })


def busqueda(request):

    print(request.GET)
    if(request.GET != {}):

        try:
            empty = False
            consulta = Curso.objects.filter(numero_cursada = request.GET['busqueda'])
            
            if(len(consulta) == 0):
                empty = True

            return render(request, 'busqueda.html', {
                'consulta' : consulta, 'empty' : empty
            })
        except:
            return render(request, 'busqueda.html', {
                'error' : 'Se ha producido un error'
            })
    else:
        print("vacio")
        return render(request, 'busqueda.html' )

   
    """ else:
        try:
            empty = False
            consulta = Curso.objects.filter(numero_cursada = request.POST['busqueda'])
            #print("Ejemplo", request.POST['busqueda'])
            
            if(len(consulta) == 0):
                empty = True

            return render(request, 'busqueda.html', {

                'consulta' : consulta, 'empty' : empty
            })
        except:
            return render(request, 'busqueda.html', {

                'error' : 'Se ha producido un error'
            }) """
