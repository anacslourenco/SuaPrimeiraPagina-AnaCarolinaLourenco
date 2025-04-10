
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class UsuarioPersonalizado(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    biografia = models.TextField(null=True, blank=True)
    # link = models.URLField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            avatar_path = self.avatar.path
            with Image.open(avatar_path) as img:
                max_size = (200, 200)
                img.thumbnail(max_size)
                img.save(avatar_path)
