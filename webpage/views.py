
from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html')

def calendario(request):
    return render(request, 'calendario.html')
def amenities(request):
    return render(request, 'comodidades.html')
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
    
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Sitemap: https://stanzadellanonna.com.ar/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def sitemap_xml(request):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://stanzadellanonna.com.ar/es/</loc>
    <lastmod>2025-06-29T22:14:37+01:00</lastmod>
    <changefreq>always</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://stanzadellanonna.com.ar/es/contacto/</loc>
    <lastmod>2025-06-29T22:14:37+01:00</lastmod>
    <changefreq>always</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://stanzadellanonna.com.ar/es/galeria/</loc>
    <lastmod>2025-06-29T22:14:37+01:00</lastmod>
    <changefreq>always</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://stanzadellanonna.com.ar/en/</loc>
    <lastmod>2025-06-27T22:14:37+01:00</lastmod>
    <changefreq>always</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://stanzadellanonna.com.ar/en/contacto/</loc>
    <lastmod>2025-06-29T22:14:37+01:00</lastmod>
    <changefreq>always</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://stanzadellanonna.com.ar/en/galeria/</loc>
    <lastmod>2025-06-27T22:14:37+01:00</lastmod>
    <changefreq>always</changefreq>
    <priority>0.8</priority>
  </url>

</urlset>
"""
    return HttpResponse(xml, content_type="application/xml")