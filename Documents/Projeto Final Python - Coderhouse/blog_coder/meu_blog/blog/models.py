
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class BasePost(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = RichTextField()
    imagem = models.ImageField(upload_to='posts/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Pagina(BasePost):
    subtitulo = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"

class Post(BasePost):
    def __str__(self):
        return self.titulo
    

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_accounts')  # Adicionado related_name
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return '/static/images/default-avatar.png'


class Mensagem(models.Model):
    remetente = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mensagens_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='mensagens_recebidas', on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensagem de {self.remetente} para {self.destinatario}"

    class Meta:
        ordering = ['-data_envio']
        indexes = [models.Index(fields=['data_envio'])]


class BlogPerfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_blog')  # Adicionado related_name
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return '/static/images/default-avatar.png'
