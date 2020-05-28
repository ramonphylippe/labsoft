from django.db import models


class Usuario(models.Model):
    usuarioNome = models.CharField('Nome', max_length=16, blank='false')
    telefone = models.CharField('telefone - principal', max_length=12, blank='false')
    cep = models.CharField('CEP', max_length=9, blank='false')
    usuarioEmail = models.EmailField('email', max_length=64, blank='false', unique='true')
    usuarioSenha = models.CharField('senha', max_length=32, blank='false')
    usuarioStatus = models.BooleanField('Usuario ativo', default='True')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.usuarioEmail


class Produto(models.Model):
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produtoNome = models.CharField('Produto', max_length=16, blank='false')
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    estoque = models.DecimalField('estoque', max_digits=4, decimal_places=0)
    produtoStatus = models.BooleanField('Produto ativo', default='true')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.produtoNome}'
