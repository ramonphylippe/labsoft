from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from .forms import ProdutoModelForm, UsuarioModelForm
from .models import Usuario, Produto


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def get_usuario(request):
    if str(request.method) == 'GET':
        usuarios = Usuario.objects.all().values()
        usuarios_lista = list(usuarios)

        return JsonResponse(usuarios_lista, safe=False)
    else:
        # print("Método não permido")
        return HttpResponse(status=405)


@csrf_exempt
def get_produtos(request):
    if str(request.method) == 'GET':
        produtos = Produto.objects.all().values()
        produtos_lista = list(produtos)

        return JsonResponse(produtos_lista, safe=False)
    else:
        # print("Método não permido")
        return HttpResponse(status=405)


@csrf_exempt
def registrarusuario(request):
    if str(request.method) == "POST":
        form = UsuarioModelForm(request.POST or None)
        if form.is_valid():
            form.save()

        else:
            print("Formulario incorreto")
            return HttpResponse(status=406)
    else:
        print("Método não permido")
        return HttpResponse(status=405)

    return render(request, 'usuario.html')


@csrf_exempt
def registrarproduto(request):
    if str(request.method) == "POST":
        form = ProdutoModelForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            print("Formulario incorreto")
            return HttpResponse(status=406)
    else:
        print("Método não permido")
        return HttpResponse(status=405)

    return HttpResponse(status=200)
