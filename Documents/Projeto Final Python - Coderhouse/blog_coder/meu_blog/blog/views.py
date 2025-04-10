
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagina, Post, Mensagem, Perfil
from .forms import PaginaForm, PostForm, PerfilForm, UserUpdateForm, PerfilUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import InscricaoForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Lista de páginas
class ListaPaginasView(ListView):
    model = Pagina
    template_name = 'lista_paginas.html'
    context_object_name = 'paginas'

    def get_queryset(self):
        return Pagina.objects.all()

# Detalhes da página
class DetalhesPaginaView(DetailView):
    model = Pagina
    template_name = 'detalhes_pagina.html'
    context_object_name = 'pagina'

# Criar página - Apenas usuários logados
class CriarPaginaView(LoginRequiredMixin, CreateView):
    model = Pagina
    form_class = PaginaForm
    template_name = 'criar_pagina.html'
    login_url = '/login/'
    success_url = reverse_lazy('lista_paginas')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Página criada com sucesso!")
        return response

# Editar página - Apenas autor pode editar
class EditarPaginaView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pagina
    form_class = PaginaForm
    template_name = 'editar_pagina.html'
    success_url = reverse_lazy('lista_paginas')

    def test_func(self):
        pagina = self.get_object()
        return self.request.user == pagina.autor

    def form_valid(self, form):
        messages.success(self.request, "Página editada com sucesso!")
        return super().form_valid(form)

# Excluir página - Apenas autor pode excluir
class ExcluirPaginaView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pagina
    template_name = 'excluir_pagina.html'
    context_object_name = 'pagina'
    success_url = reverse_lazy('lista_paginas')

    def test_func(self):
        pagina = self.get_object()
        return self.request.user == pagina.autor

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Página excluída com sucesso!")
        return super().delete(request, *args, **kwargs)

@login_required
def perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    return render(request, 'perfil.html', {'perfil': perfil})

@login_required
def lista_mensagens(request):
    mensagens = Mensagem.objects.filter(destinatario=request.user).order_by('-data_envio')
    return render(request, 'lista_mensagens.html', {'mensagens': mensagens})

@login_required
def enviar_mensagem(request, destinatario_id):
    destinatario = get_object_or_404(User, id=destinatario_id)
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        Mensagem.objects.create(remetente=request.user, destinatario=destinatario, conteudo=conteudo)
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('lista_mensagens')

    return render(request, 'enviar_mensagem.html', {'destinatario': destinatario})

@login_required
def detalhes_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, id=mensagem_id, destinatario=request.user)
    mensagem.lida = True
    mensagem.save()
    return render(request, 'detalhes_mensagem.html', {'mensagem': mensagem})

@login_required
def confirmar_exclusao(request, pagina_id):
    pagina = get_object_or_404(Pagina, id=pagina_id)
    if request.user != pagina.autor:
        return HttpResponseForbidden("Você não tem permissão para excluir esta página.")

    if request.method == 'POST':
        pagina.delete()
        messages.success(request, "Página excluída com sucesso!")
        return redirect('lista_paginas')

    return render(request, 'confirmar_exclusao.html', {'pagina': pagina})

@login_required
def atualizar_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    if request.method == "POST":
        form = PerfilUpdateForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('perfil')
    else:
        form = PerfilUpdateForm(instance=perfil)

    return render(request, 'accounts/atualizar_perfil.html', {'form': form})


def inscrever(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  #Login automático após o registro
            messages.success(request, 'Conta criada com sucesso! Bem-vindo(a), {}!'.format(user.username))
            return redirect('home')
        else:
            messages.error(request, 'Erro ao criar a conta. Verifique os dados e tente novamente.')
    else:
        form = InscricaoForm()

    return render(request, 'inscrever.html', {'form': form})


@login_required
def visualizar_perfil(request):
    perfil = request.user.perfil
    return render(request, 'accounts/perfil.html', {'perfil': perfil})


def criar_post(request):
    if request.method == 'POST':
        return HttpResponse("Post criado com sucesso!")
    return render(request, 'criar_post.html')
