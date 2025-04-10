
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PerfilForm, RegistroForm
from django.contrib import messages
from .models import UsuarioPersonalizado
from django.contrib.auth.forms import UserCreationForm
from .forms import EditarPerfilForm



class UsuarioPersonalizadoCreationForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ('username', 'email')


def visualizar_perfil(request, id):
    usuario = get_object_or_404(UsuarioPersonalizado, id=id)
    return render(request, "registration/perfil.html", {"usuario": usuario})


def register_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Agora você pode fazer login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao criar conta. Verifique os dados e tente novamente.')
    else:
        form = RegistroForm()

    return render(request, 'registration/inscrever.html', {'form': form})


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('perfil_usuario')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'registration/editar_perfil.html', {'form': form})


@login_required
def perfil_usuario(request):
    return render(request, 'registration/perfil.html', {'usuario': request.user})

