
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado


class PerfilForm(forms.ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = [
            'first_name', 'last_name', 'username', 'email',
            'avatar', 'biografia', 'data_nascimento'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu sobrenome'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@dominio.com'
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'biografia': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Fale um pouco sobre você',
                'rows': 3
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class EditarPerfilForm(PerfilForm):
    pass


class RegistroForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escolha um nome de usuário'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@dominio.com'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha'
            }),
        }
