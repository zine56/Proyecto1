from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    
    return render(request, 'AppPrueba/inicio.html', {})