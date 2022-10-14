from http.client import HTTPResponse
from django.shortcuts import render


def conta_view(request):
    teste = 'teste'
    context = {
        'teste':teste
    }
    return render(request, 'conta_view.html', context)