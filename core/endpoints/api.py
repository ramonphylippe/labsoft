from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from core.models import Produto, Usuario


class ProdutoResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id produto': 'id',
        'id vendedor': 'vendedor.id',
        'Produto': 'produtoNome',
        'Valor': 'valor',
    })

    def list(self):
        return Produto.objects.all()

    def detail(self, pk):
        return Produto.object.get(id=pk)

    def create(self):
        return Produto.object.create(
            vendedor=Usuario.object.get(name=self.data['usuarioNome']),
            produto=self.data['produtoNome'],
            valor=self.data['valor']
        )
