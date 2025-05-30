from bs4 import BeautifulSoup
import os

# Ruta a tu carpeta con los archivos HTML
RUTA_CARPETA = "templates"

# Si querés guardar el archivo CSS generado
GUARDAR_CSS = True
NOMBRE_ARCHIVO_CSS = "estilos-generados.css"

# Set para guardar todas las clases encontradas
todas_las_clases = set()

# Recorrer todos los archivos HTML en la carpeta
for archivo in os.listdir(RUTA_CARPETA):
    if archivo.endswith(".html"):
        with open(os.path.join(RUTA_CARPETA, archivo), "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            for tag in soup.find_all(True):
                clases = tag.get("class", [])
                for clase in clases:
                    todas_las_clases.add(clase)

# Mostrar en consola
print("Clases encontradas:")
for clase in sorted(todas_las_clases):
    print(f".{clase} {{}}")

# Guardar como archivo .css (opcional)
if GUARDAR_CSS:
    with open(NOMBRE_ARCHIVO_CSS, "w", encoding="utf-8") as f:
        for clase in sorted(todas_las_clases):
            f.write(f".{clase} {{\n    \n}}\n")
    print(f"\n✅ Archivo generado: {NOMBRE_ARCHIVO_CSS}")
