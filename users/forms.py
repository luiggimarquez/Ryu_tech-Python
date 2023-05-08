from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Usuario", max_length=20,required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Apellido", max_length=20,required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="Nombre", max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:

        model = User
        fields = ['username', 'email','first_name','last_name','password1','password2']
        help_texts = {k:"" for k in fields}
