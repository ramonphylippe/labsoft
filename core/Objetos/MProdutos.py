import datetime
from django.core import serializers
from django.http import HttpResponse
from core.models import Produto as produtoModel, UserProfile as vendedorPerfil


def invalidarProdutos():
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    produtoModel.objects.filter(produtoStatus='True', criado=date_from).update(produtoStatus=False)


# retorna todos os produtos ativos
def getProdutos():
    invalidarProdutos()
    data = produtoModel.objects.filter(produtoStatus='True')
    data_list = serializers.serialize("json", data, fields=('produtoNome', 'valor', 'produtoDescricao', 'produtoImagem', 'criado'))

    return HttpResponse(data_list)


# retorna os produtos do usuario
def getProdutosById(idFromToken):
    vendedor = vendedorPerfil.objects.get(user_id=idFromToken)

    data = produtoModel.objects.filter(vendedor_id=vendedor.id, produtoStatus='True')
    data_list = serializers.serialize("json", data, fields=('id', 'vendedor', 'produtoNome', 'valor', 'produtoDescricao', 'produtoImagem'))

    return HttpResponse(data_list)


# retorna os produtos do usuario que estão inativos/deletados
# não tem uso ainda
def getProdutosByIdAndDisabled(idFromToken):
    vendedor = vendedorPerfil.objects.get(user_id=idFromToken)
    data = produtoModel.objects.filter(vendedor_id=vendedor.id, produtoStatus='False')
    data_list = serializers.serialize("json", data, fields=('id', 'vendedor', 'produtoNome', 'valor', 'produtoDescricao', 'produtoImagem'))

    return HttpResponse(data_list)


def deletarProduto(idProduto, idFromToken):
    try:
        vendedor = vendedorPerfil.objects.get(user_id=idFromToken)
        print(idProduto, "\n", idFromToken)
        produtoModel.objects.filter(pk=idProduto, vendedor_id=vendedor.id).update(produtoStatus=False)
        return bool(True)
    except:
        print(Exception)
        return bool(False)
