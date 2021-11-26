from django.urls.conf import path
from .views import inicio, lista_casas, lista_mascotas, crear_casa

urlpatterns = [
    path('', inicio, name='inicio'),
    path('casas/', lista_casas, name='Casas'),
    path('casas/crear/', crear_casa, name='Crear_casa'),
    path('mascotas/', lista_mascotas, name='Mascotas'),
    # path('vecinos/', lista_vecinos, name='Vecinos')
]
