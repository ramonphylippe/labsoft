from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('usuario/cadastrar', cadastrarusuario, name='cadastrar usuario'),

    path('produto/listar', getProdutosTodos, name='Listar os produtos armazenados'),
    path('produto/listarDoUsuario', getProdutosDoUsuario, name='Listar os produtos armazenado pelo id do vendedor'),
    path('produto/cadastrar', putproduto, name='cadastrar produto'),
    path('produto/atualizar', updateproduto, name='Atualizar um produto do usuario')

]
