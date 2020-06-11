from django.contrib.auth.decorators import login_required
from .models import Produto
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import Group
from core.forms import ProdutoModelForm, UserProfileForm, ExtendedUserCreationForm
from core.recursos import tokenJwt
from core.Objetos import MProdutos


def index(request):
    return render(request, 'index.html')


@require_http_methods(["POST"])
def cadastrarusuario(request):
    form = ExtendedUserCreationForm(request.POST)
    profile_form = UserProfileForm(request.POST)
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
        form = ProdutoModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("Formulario correto\nProduto cadastrado corretamente")
            return HttpResponse(status=200)
        else:
            print("Formulario incorreto")
            print(form.fields)
            return HttpResponse(status=406)
    else:
        print("Não Aceitavel")
        return HttpResponse(status=406)


@csrf_exempt
@require_http_methods(["POST"])
def updateproduto(request):
    if ('jwtToken' in request.headers) and ('idDoProduto' in request.headers) and ('produtoNome' in request.headers) \
            and ('valor' in request.headers) and tokenJwt.checkTokenValidation(request.headers['jwtToken']):

        atualizado = MProdutos.updateProdutoAtributos(request.headers['idDoProduto'], request.headers['produtoNome'], request.headers['valor'])
    else:
        atualizado = bool(False)
    return HttpResponse(status=200) if atualizado else HttpResponse(status=406)
