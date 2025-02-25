
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Post, Comentario
from .forms import CategoriaForm, PostForm, ComentarioForm

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def cria_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/cria_post.html', {'form': form})

def cria_comentario(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('lista_posts')
    else:
        form = ComentarioForm()
    return render(request, 'blog/cria_comentario.html', {'form': form, 'post': post})

def cria_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')  # ou para outra página desejada
    else:
        form = CategoriaForm()
    return render(request, 'blog/cria_categoria.html', {'form': form})

def detalhe_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalhe_post.html', {'post': post})

def teste_template(request):
    return render(request, 'blog/teste.html')
