from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import Group
from core.models import Produto
from core import forms
from core.recursos import tokenJwt
from core.Objetos import MProdutos


def index(request):
    return render(request, 'index.html')

@csrf_exempt
@require_http_methods(["POST"])
def cadastrarusuario(request):
    form = forms.ExtendedUserCreationForm(request.POST)
    profile_form = forms.UserProfileForm(request.POST)
    if form.is_valid() and profile_form.is_valid():
        user = form.save()

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        group_default = Group.objects.get(name='usuarioVendedor')
        group_default.user_set.add(user)
    else:
        print(form.fields)
        print(profile_form.fields)
        print("Formulario incorreto")
        return HttpResponse(status=406)

    return HttpResponse(status=200)


@csrf_exempt
@require_http_methods(["GET"])
def getProdutosTodos(request):
    return HttpResponse(MProdutos.getProdutos())


@csrf_exempt
@require_http_methods(["POST"])
def getProdutosDoUsuario(request):
    if 'jwtToken' in request.headers:
        idtemp = tokenJwt.getIdFromToken(request.headers['jwtToken'])
        if idtemp:
            data = MProdutos.getProdutosById(idtemp)
            return HttpResponse(data)
        else:
            return HttpResponse(status=401)
    else:
        print("Não Aceitavel")
        return HttpResponse(status=406)


@csrf_exempt
@require_http_methods(["POST"])
def putproduto(request):
    if ('jwtToken' in request.headers) and (tokenJwt.checkTokenValidation(request.headers['jwtToken'])):
        form = forms.ProdutoModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("Formulario correto\nProduto cadastrado corretamente")
            return HttpResponse(status=200)
        else:
            print("Formulario incorreto\nProduto não foi cadastrado: ", form.errors)
            return HttpResponse(status=406)
    else:
        print("Requisição não aceitavel")
        return HttpResponse(status=406)


@csrf_exempt
@require_http_methods(["POST"])
def editproduto(request):
    if ('jwtToken' in request.headers) and (tokenJwt.checkTokenValidation(request.headers['jwtToken'])):
        item = Produto.objects.get(pk=request.headers['idDoProduto'])
        form = forms.ProdutoModelFormEdit(request.POST)
        if form.is_valid():

            form = forms.ProdutoModelFormEdit(request.POST, instance=item)
            form.save()
            msg = "Formulario correto\nProduto atualizado corretamente"
            print(msg)
            return HttpResponse(msg, status=200)
        else:
            msg = "Formulario incorreto\nProduto não foi atualizado"
            print(msg, "\n", form.errors)
            return HttpResponse(msg, status=406)
    return HttpResponse("Token ou usuario invalido", status=406)


@csrf_exempt
@require_http_methods(["POST"])
# produtos não são deletados, seu status passa para false
def deleteproduto(request):
    sucesso = bool(False)
    if ('jwtToken' in request.headers) and (tokenJwt.checkTokenValidation(request.headers['jwtToken'])):
        sucesso = MProdutos.deletarProduto(request.headers['idDoProduto'], tokenJwt.getIdFromToken(request.headers['jwtToken']))
    else:
        return HttpResponse("Token ou usuario invalido", status=406)
    return HttpResponse(status=200) if sucesso else HttpResponse("Não foi possivel realizar a operação", status=400)
