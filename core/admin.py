from django.contrib import admin

from .models import Usuario, Produto


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuarioNome', 'usuarioEmail', 'usuarioStatus')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produtoNome', 'valor', 'vendedor', 'produtoStatus')
