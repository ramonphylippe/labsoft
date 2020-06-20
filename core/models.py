from django.contrib.auth.models import User
from django.db import models
from stdimage.models import StdImageField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.BigIntegerField('telefone')
    cep = models.PositiveIntegerField('cep')

    def __str__(self):
        return self.user.username


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)

    class Meta:
        abstract = True


class Produto(Base):
    vendedor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    produtoNome = models.CharField('Produto', max_length=32, blank='false')
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    produtoStatus = models.BooleanField('Produto ativo', default='true')
    produtoDescricao = models.CharField('Descrição', max_length=320, default='')
    produtoImagem = StdImageField('Imagem', upload_to='core/Objetos/img-produtos', variations={'thumb': (124, 124)},
                                  default='core/Objetos/img-produtos/default.jpg')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.produtoNome}'
