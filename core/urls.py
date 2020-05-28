from django.urls import path
from .views import index, get_usuario, get_produtos, registrarusuario, registrarproduto

urlpatterns = [
    path('', index, name='index'),
    path('usuario/listar', get_usuario, name='usuario'),
    path('usuario/registrar', registrarusuario, name='usuario registrar'),
    path('produto/listar', get_produtos, name='produto'),
    path('produto/registrar', registrarproduto, name='produto registrar'),
]
