from django import forms
from core.models import Produto, Usuario


class UsuarioForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=16)
    telefone = forms.CharField(label='Contato', max_length=12)
    cep = forms.CharField(label='Cep', max_length=9)
    email = forms.CharField(label='email', max_length=64)
    senha = forms.CharField(label='senha', max_length=32)


class UsuarioModelForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['usuarioNome', 'telefone', 'cep', 'usuarioEmail', 'usuarioSenha', 'usuarioStatus']


class ProdutoForm(forms.Form):
    vendedor = forms.CharField(label='idVendedor')
    nome = forms.CharField(label='nome')
    valor = forms.CharField(label='valor')
    estoque = forms.CharField(label='estoque')
    status = forms.CharField(label='status')


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['vendedor', 'produtoNome', 'valor', 'estoque', 'produtoStatus']
