from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('produto/listar', get_produtos, name='produto'),
    path('produto/registrar', registrarproduto, name='produto registrar'),
    path('usuario/cadastrar', cadastrarusuario, name='cadastrar_usuario'),
]
