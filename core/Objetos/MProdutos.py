from django.core import serializers
from django.http import HttpResponse
from core.models import Produto as produtoModel


# retorna todos os produtos ativos
def getProdutos():
    data = produtoModel.objects.filter(produtoStatus='True')
    data_list = serializers.serialize("json", data, fields=('produtoNome', 'valor', 'produtoDescricao'))

    return HttpResponse(data_list)


# retorna os produtos do usuario
def getProdutosById(idFromToken):
    data = produtoModel.objects.filter(vendedor_id=idFromToken, produtoStatus='True')
    data_list = serializers.serialize("json", data, fields=('id', 'vendedor', 'produtoNome', 'valor', 'produtoDescricao'))

    return HttpResponse(data_list)


# retorna os produtos do usuario que estão inativos/deletados
# não tem uso ainda
def getProdutosByIdAndDisabled(idFromToken):
    data = produtoModel.objects.filter(vendedor_id=idFromToken, produtoStatus='False')
    data_list = serializers.serialize("json", data, fields=('id', 'vendedor', 'produtoNome', 'valor', 'produtoDescricao'))

    return HttpResponse(data_list)


def deletarProduto(idProduto, idFromToken):
    try:
        produtoModel.objects.filter(pk=idProduto, vendedor_id=idFromToken).update(produtoStatus=False)
        return bool(True)
    except:
        return bool(False)
