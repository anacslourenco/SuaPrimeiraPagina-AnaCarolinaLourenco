
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import inscrever
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import ListaPaginasView, DetalhesPaginaView, CriarPaginaView, EditarPaginaView, ExcluirPaginaView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),
    
    # Página sobre
    path('about/', views.about, name='about'),

    # Páginas
    path('pages/', ListaPaginasView.as_view(), name='lista_paginas'),
    path('pages/<int:pk>/', DetalhesPaginaView.as_view(), name='detalhes_pagina'),

    # Criar, editar e excluir páginas
    path('criar/', CriarPaginaView.as_view(), name='criar_pagina'),
    path('editar/<int:pk>/', EditarPaginaView.as_view(), name='editar_pagina'),
    path('excluir/<int:pk>/', ExcluirPaginaView.as_view(), name='excluir_pagina'),

    # Criar post
    path('criar_post/', views.criar_post, name='criar_post'),

    # Inscrever-se
    path('inscrever/', inscrever, name='inscrever'),

    # Perfil do usuário
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/atualizar/', views.atualizar_perfil, name='atualizar_perfil'),

    # Autenticação
    path('login/', auth_views.LoginView.as_view(next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Admin
    path('admin/', admin.site.urls, name='admin_custom'),
    path('accounts/', include('accounts.urls')),

    # Alterar senha
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Mensagens
    path('mensagens/', views.lista_mensagens, name='lista_mensagens'),
    path('mensagem/enviar/<int:destinatario_id>/', views.enviar_mensagem, name='enviar_mensagem'),
    path('mensagem/<int:mensagem_id>/', views.detalhes_mensagem, name='detalhes_mensagem'),

    path('pagina/confirmar_exclusao/<int:pagina_id>/', views.confirmar_exclusao, name='confirmar_exclusao'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
