from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EstudiantesForm, ProfesoresForm, CursosForm
from .models import Curso
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def base(request):
    hero = True
    return render(request, 'index.html',{
            'hero': hero, 'about':True
    })


def signup(request):

    if(request.user.is_authenticated):
        return redirect('home')
    else:

        if (request.method == 'GET'):
            return render(request, "signUp.html",{
            'form': UserCreationForm
            })
        else:

            if(request.POST['password1'] == request.POST['password2']):
                try:
                    user = User.objects.create_user(username=request.POST['username'].lower(), password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('home')
                except:
                    return render(request, "signUp.html",{
                    'form': UserCreationForm, 'errors':'Usuario ya Existe'
                    })

            else:
                return render(request, "signUp.html",{
                'form': UserCreationForm, 'errors':'Password no coinciden'
                })

@login_required         
def log_out(request):
    logout(request)
    return redirect('home')


def log_in(request):

    if(request.user.is_authenticated):
        return redirect('home')
    else:
        if(request.method == 'GET'):

            return render(request, "login.html",{
                'form': AuthenticationForm
            })
        else:

            user = authenticate(request,username=request.POST['username'].lower(), password=request.POST['password'])

            if(user is None):
                return render(request, "login.html",{
                'form': AuthenticationForm, 'errors':"Usuario/Password erróneo"
            })
            else:
                login(request, user)
                return redirect('home')

@login_required    
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

@login_required
def profesores(request):

    if(request.method == 'GET'):
        return render(request, "profesores.html",{
            'form': ProfesoresForm
        })
    else:
        form = ProfesoresForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, "profesores.html",{
                'form': ProfesoresForm, 'saved':"Datos almacenados correctamente"
            })
        else:
            return render(request, "profesores.html",{
            'form': ProfesoresForm, 'errors': form.errors
        })
     
@login_required
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

@login_required
def busqueda(request):

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
                'error' : 'Se ha producido un error, respuesta en blanco o dato incorrecto'
            })
    else:
        print("vacio")
        return render(request, 'busqueda.html' )
