
from django.urls import path
from .views import lista_posts, cria_post, cria_comentario, cria_categoria, detalhe_post

urlpatterns = [
    path('', lista_posts, name='lista_posts'),
    path('cria_post/', cria_post, name='cria_post'),
    path('cria_comentario/<int:post_id>/', cria_comentario, name='cria_comentario'),
    path('post/<int:post_id>/', detalhe_post, name='detalhe_post'),
    path('cria_categoria/', cria_categoria, name='cria_categoria'),
]
