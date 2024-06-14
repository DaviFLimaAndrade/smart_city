from django.shortcuts import render
from django.http import HttpResponse

def abre_index(request):
    mensagem = "Termineiiiiiii!"
    return HttpResponse(mensagem)