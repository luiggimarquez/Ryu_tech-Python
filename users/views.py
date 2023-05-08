from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

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
            'form': UserRegisterForm
            })
        else:

            if(request.POST['password1'] == request.POST['password2']):
                try:
                    form = UserRegisterForm(request.POST)
                    print(form)
                    print("por entrar")
                    if form.is_valid():
                        print("entro")
                        info = form.cleaned_data
                        print(info)
                        user = User.objects.create_user(username=str(info['username']).lower(), password=str(info['password1']), first_name=str(info['first_name']), last_name=str(info['last_name']), email=str(info['email']))
                        user.save()
                        login(request, user)
                        return redirect('home')
                    else:
                        print(form.errors)
                        return render(request, "signUp.html",{
                        'form': UserRegisterForm, 'errors':form.errors
                    })
                except:
                    return render(request, "signUp.html",{
                    'form': UserRegisterForm, 'errors':'Usuario ya Existe'
                    })

            else:
                return render(request, "signUp.html",{
                'form': UserRegisterForm, 'errors':'Password no coinciden'
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
            
class profile(UpdateView):
   
    template_name = 'profile.html'
    model = Profile
    fields = [ 'avatar', 'bio', 'link', 'first_name']
    success_url = reverse_lazy('profile')

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user = self.request.user)
        return profile
    
    """
     if(request.user.is_authenticated):
        print(request.user.userprofile.username)
        return render(request,"profile.html", {

            'user_logged' : request.user
        })
    else:
        return redirect("login") """
