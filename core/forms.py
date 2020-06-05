from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import Produto, UserProfile


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('telefone', 'cep')


class ProdutoForm(forms.Form):
    vendedor = forms.CharField(label='idVendedor')
    nome = forms.CharField(label='nome')
    valor = forms.CharField(label='valor')
    status = forms.CharField(label='status')


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['vendedor', 'produtoNome', 'valor', 'produtoStatus']
