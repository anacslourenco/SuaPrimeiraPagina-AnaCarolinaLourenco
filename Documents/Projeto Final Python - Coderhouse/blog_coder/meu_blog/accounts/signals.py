
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UsuarioPersonalizado


@receiver(post_save, sender=UsuarioPersonalizado)
def criar_usuario_personalizado(sender, instance, created, **kwargs):
    if created:
        if not instance.biografia:
            instance.biografia = "Olá, acabei de criar meu perfil!"
        instance.save()


@receiver(post_save, sender=UsuarioPersonalizado)
def atualizar_usuario_personalizado(sender, instance, **kwargs):
    if instance.username and not instance.first_name:
        instance.first_name = instance.username.capitalize()
        instance.save()


