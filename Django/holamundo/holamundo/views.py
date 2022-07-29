from django.template.context_processors import request
from django.http.response import HttpResponse
def saludo(request):
    return HttpResponse("Hola mundo desde Asturias")
    
def despedida(request):
    return HttpResponse('Despedida desde Asturias')
def adulto(request, edad):
    if edad>=18:
        return HttpResponse('Eres mayor de edad')
    else:
        return HttpResponse('Eres menor de edad')