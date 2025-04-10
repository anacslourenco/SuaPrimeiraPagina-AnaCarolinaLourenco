
from django.contrib import admin
from django.utils.html import format_html
from .models import Pagina, Post, Perfil

class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'data_publicacao')
    search_fields = ('titulo', 'subtitulo')
    list_filter = ('data_publicacao',)
    date_hierarchy = 'data_publicacao'


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'imagem_preview')
    search_fields = ('titulo',)
    date_hierarchy = 'data_publicacao'

    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;"/>', obj.imagem.url)
        return "Sem imagem"
    imagem_preview.short_description = 'Imagem'


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'biography', 'avatar_preview')
    search_fields = ('user__username',)

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:50%;"/>', obj.avatar.url)
        return "Sem avatar"
    avatar_preview.short_description = 'Avatar'


admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Perfil, PerfilAdmin)

