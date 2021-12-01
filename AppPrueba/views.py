from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Casa, Mascota, Vecino
from .forms import CasasFormulario, VecinosFormulario, MascotasFormulario 

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

def crear_mascota(request):
    
    if request.method == 'POST':
        formulario = MascotasFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            mascota = Mascota(nombre=datos['nombre'], edad=datos['edad'], animal=datos['animal'])
            mascota.save()
            return redirect('Mascotas')
    
    formulario = MascotasFormulario()
    return render(request, 'AppPrueba/formulario_mascota.html', {'formulario': formulario})

def lista_vecinos(request):
    vecinos = None
    error = None
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        if nombre == '':
            vecinos = Vecino.objects.all()
        else:
            vecinos = Vecino.objects.filter(nombre=nombre)

        
    return render(request, 'AppPrueba/lista_vecinos.html', {'vecinos': vecinos, 'error': error})

def crear_vecino(request):
    
    if request.method == 'POST':
        formulario = VecinosFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            vecino = Vecino(nombre=datos['nombre'], numero=datos['numero'], apellido=datos['apellido'])
            vecino.save()
            return redirect('Vecinos')
    
    formulario = VecinosFormulario()
    return render(request, 'AppPrueba/formulario_vecino.html', {'formulario': formulario})
