from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import Group
from .forms import ProdutoModelForm, UserProfileForm, ExtendedUserCreationForm
from .models import Produto


def index(request):
    return render(request, 'index.html')


# @csrf_exempt
# def get_usuario(request):
#     if str(request.method) == 'GET':
#         usuarios = User.objects.all().values()
#         usuarios_lista = list(usuarios)
#
#         return JsonResponse(usuarios_lista, safe=False)
#     else:
#         # print("Método não permido")
#         return HttpResponse(status=405)


@csrf_exempt
#@login_required
#@require_http_methods({"GET"})
def get_produtos(request):
    if str(request.method) == 'GET':
        produtos = Produto.objects.all().values()
        produtos_lista = list(produtos)

        return JsonResponse(produtos_lista, safe=False)
    else:
        # print("Método não permido")
        return HttpResponse(status=405)


@csrf_exempt
def cadastrarusuario(request):
    if request.method == "POST":
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
    else:
        print("Método não permido")
        return HttpResponse(status=405)
    return HttpResponse(status=200)


@csrf_exempt
def registrarproduto(request):
    if str(request.method) == "POST":
        form = ProdutoModelForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            print("Formulario incorreto")
            print(form.fields)
            return HttpResponse(status=406)
    else:
        print("Método não permido")
        return HttpResponse(status=405)

    return HttpResponse(status=200)



