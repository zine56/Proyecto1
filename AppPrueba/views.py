from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Casa, Mascota
from .forms import CasasFormulario

# Create your views here.

def inicio(request):
    return render(request, 'AppPrueba/inicio.html', {})

def lista_casas(request):
    casas = None
    error = None
    if request.method == 'GET':
        numero = request.GET.get('numero', '')
        if numero == '':
            casas = Casa.objects.all()
        else:
            try:
                numero = int(numero)
                casas = Casa.objects.filter(numero=numero)
            except:
                error = 'Debes ingresasr un numero entero.'

        
    return render(request, 'AppPrueba/lista_casas.html', {'casas': casas, 'error': error})

def crear_casa(request):
    
    if request.method == 'POST':
        formulario = CasasFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            casa = Casa(escaleras=datos['escaleras'], numero=datos['numero'], cant_ventanas=datos['cant_ventanas'])
            casa.save()
            return redirect('Casas')
    
    formulario = CasasFormulario()
    return render(request, 'AppPrueba/formulario_casa.html', {'formulario': formulario})

def lista_mascotas(request):
    mascotas = None
    error = None
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        if nombre == '':
            mascotas = Mascota.objects.all()
        else:
            mascotas = Mascota.objects.filter(nombre=nombre)

        
    return render(request, 'AppPrueba/lista_mascotas.html', {'mascotas': mascotas, 'error': error})
