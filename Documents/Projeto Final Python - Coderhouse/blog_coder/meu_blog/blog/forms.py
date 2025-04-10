
from django import forms
from django.contrib.auth.models import User
from .models import Pagina, Post, Perfil
from django.contrib.auth.forms import UserCreationForm


class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['titulo', 'subtitulo', 'conteudo', 'imagem']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'imagem']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PerfilForm(forms.ModelForm):  
    class Meta:
        model = Perfil 
        fields = ['avatar', 'biography']


class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biography']


class InscricaoForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Informe um e-mail válido.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']