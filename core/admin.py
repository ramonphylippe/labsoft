from django.contrib import admin
from .models import UserProfile, Produto

# admin.site.register(UserProfile)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produtoNome', 'valor', 'vendedor', 'produtoStatus', 'produtoImagem')
