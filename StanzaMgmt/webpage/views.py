
from django.shortcuts import render
from django.http import JsonResponse

# def index(request):
#     return render(request, 'index.html')

def calendario(request):
    return render(request, 'calendario.html')
def contacto(request):
    return render(request, 'contacto.html')
def galeria(request):
    return listar_imagenes(request, subcarpeta="")

from django.views.decorators.cache import cache_page

@cache_page(300)  # 5 minutos
def index(request):
    return render(request, "index.html")


from django.conf import settings
import os

from functools import lru_cache

@lru_cache(maxsize=32)
def obtener_listado(subcarpeta=""):
    ruta_base = os.path.join(settings.STATICFILES_DIRS[0], "imagenes", subcarpeta)
    if not os.path.exists(ruta_base):
        return [], []

    archivos = sorted(os.listdir(ruta_base))
    imagenes = [
        os.path.join("imagenes", subcarpeta, archivo).replace("\\", "/").strip("/")
        for archivo in archivos
        if archivo.lower().endswith((".webp"))
        and os.path.isfile(os.path.join(ruta_base, archivo))
    ]
    carpetas = [
        archivo for archivo in archivos
        if os.path.isdir(os.path.join(ruta_base, archivo))
    ]
    return imagenes, carpetas

def listar_imagenes(request, subcarpeta=""):
    imagenes, carpetas = obtener_listado(subcarpeta)
    if not imagenes and not carpetas:
        return render(request, "index.html", {"mensaje": "Carpeta no encontrada"})

    return render(request, "galeria.html", {
        "imagenes": imagenes,
        "carpetas": carpetas,
        "subcarpeta": subcarpeta
    })