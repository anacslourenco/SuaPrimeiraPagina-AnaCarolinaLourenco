
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Pagina, Post
from django.contrib.auth.models import User


# Para quando uma página for salva
@receiver(post_save, sender=Pagina)
def pagina_salva(sender, instance, created, **kwargs):
    if created:
        print(f"A nova página '{instance.titulo}' foi criada.")
    else:
        print(f"A página '{instance.titulo}' foi atualizada.")

# Para quando uma página for excluída
@receiver(post_delete, sender=Pagina)
def pagina_excluida(sender, instance, **kwargs):
    print(f"A página '{instance.titulo}' foi excluída.")
