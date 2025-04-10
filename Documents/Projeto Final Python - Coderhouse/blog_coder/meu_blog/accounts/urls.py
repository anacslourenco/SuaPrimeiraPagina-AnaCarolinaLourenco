
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import visualizar_perfil, register_view, editar_perfil, perfil_usuario

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("inscrever/", register_view, name="register"),
    path("editar/", editar_perfil, name="editar_perfil"),
    path("perfil/", perfil_usuario, name="perfil_usuario"),
    path("perfil/<int:id>/", visualizar_perfil, name="visualizar_perfil"),
]
