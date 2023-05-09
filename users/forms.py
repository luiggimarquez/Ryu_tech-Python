from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.contrib.auth import get_user

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Usuario", max_length=20,required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Apellido", max_length=20,required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="Nombre", max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:

        model = User
        fields = ['username', 'email','first_name','last_name','password1','password2']
        help_texts = {k:"" for k in fields}

class editUserForm(UserCreationForm):


    email = forms.EmailField(label = "Modificar Email", required = False,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduce nuevo Email'}))
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Introduce nuevo Password'}), required = False)
    password2 = forms.CharField(label = "Repite Contraseña", widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repite nuevo Password'}), required = False)
    first_name = forms.CharField(label = "Nombre", required = False,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduce nuevo Nombre'}))
    last_name = forms.CharField(label = "Apellido", required = False,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduce nuevo Apellido'})) 

    class Meta():
        model = User
        fields = ['email','password1','password2','first_name','last_name']

        helps_text = {k:"" for k in fields}

    def __init__(self,*args,**kwargs):
        self.user = kwargs.pop('user')
        super(editUserForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'value':self.user.email, 'class':'form-control', 'placeholder':'Introduce nuevo Email'})
        
    