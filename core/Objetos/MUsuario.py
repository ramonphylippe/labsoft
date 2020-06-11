# deixei isso aqui, era uma view antiga que retornava todos os usuario cadastrados
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

