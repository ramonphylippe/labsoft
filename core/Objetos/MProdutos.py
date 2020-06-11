from django.core import serializers
from django.http import HttpResponse
from core.models import Produto as produtoModel


# retorna todos os produtos ativos
def getProdutos():
    data = produtoModel.objects.filter(produtoStatus='True')
    data_list = serializers.serialize("json", data, fields=('produtoNome', 'valor'))

    return HttpResponse(data_list)


# retorna os produtos do usuario
def getProdutosById(idFromToken):
    data = produtoModel.objects.filter(vendedor_id=idFromToken)
    data_list = serializers.serialize("json", data, fields=('id', 'vendedor', 'produtoNome', 'valor'))

    return HttpResponse(data_list)


# retorna os produtos do usuario que estão inativos/deletados
# não tem uso ainda
def getProdutosByIdAndDisabled(idFromToken):
    data = produtoModel.objects.filter(vendedor_id=idFromToken, produtoStatus='False')
    data_list = serializers.serialize("json", data, fields=('id', 'vendedor', 'produtoNome', 'valor', 'produtoStatus'))

    return HttpResponse(data_list)


# ta bugado
def updateProdutoAtributos(idProduto, novoProdutoNome, novoValor):
    try:
        nomeDaTreta = produtoModel.objects.filter(pk=idProduto)
        nomeDaTreta.produtoNome = novoProdutoNome
        nomeDaTreta.valor = novoValor
        nomeDaTreta.save()
        # nomeDaTreta.save(produtoNome=novoProdutoNome, valor=novoValor)
        return bool(True)
    except Exception:
        print("não foi possivel atualizar produto")
        return bool(False)

class verificarProdutoDoDono():
    pass