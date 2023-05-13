from django.forms import ModelForm
from .models import Posts
from django import forms
from ckeditor.fields import RichTextField, RichTextFormField

class PostsForm(ModelForm):

    title = forms.CharField(label= 'Título', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    subtitle = forms.CharField(label= 'Descripción', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    Message = RichTextFormField(label="Publicación", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    imageMain = forms.ImageField(label = 'Imagen', required=True, widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = Posts
        fields =['title','subtitle','Message','imageMain']