from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('usuario/cadastrar', cadastrarusuario, name='cadastrar usuario'),
    path('solicitarToken/', obtain_jwt_token, name='para obter o token de autenticação'),
    path('produto/listar', getProdutosTodos, name='Listar os produtos armazenados'),
    path('produto/doUsuario', getProdutosDoUsuario, name='Listar os produtos armazenado pelo id do vendedor'),
    path('produto/cadastrar', putproduto, name='cadastrar produto'),
    path('produto/atualizar', editproduto, name='Atualizar um produto do usuario'),
    path('produto/deletar', deleteproduto, name='Passa o status para falso')

]
