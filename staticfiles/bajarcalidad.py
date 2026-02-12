import os
from PIL import Image

def optimizar_imagenes(max_width=2000, calidad=85, tamano_minimo=200):
    # Obtener la carpeta actual donde se encuentra el script
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    carpeta_salida = os.path.join(carpeta_actual, "img")  # Carpeta para las imágenes optimizadas

    # Crear la carpeta de salida si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Listar todos los archivos de la carpeta actual
    archivos = os.listdir(carpeta_actual)

    for archivo in archivos:
        # Verificar si el archivo es una imagen
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            ruta_original = os.path.join(carpeta_actual, archivo)
            
            # Verificar el tamaño del archivo en KB
            tamano_archivo = os.path.getsize(ruta_original) / 1024  # Convertir bytes a KB
            if tamano_archivo > tamano_minimo:
                nombre_salida = f"{archivo.split('.')[0]}_lq.jpg"
                ruta_salida = os.path.join(carpeta_salida, nombre_salida)

                # Abrir la imagen original
                imagen = Image.open(ruta_original)

                # Redimensionar la imagen manteniendo la relación de aspecto
                width, height = imagen.size
                if width > max_width:
                    nuevo_height = int(max_width * height / width)
                    imagen = imagen.resize((max_width, nuevo_height), Image.Resampling.LANCZOS )

                # Guardar la imagen optimizada
                imagen.save(ruta_salida, "JPEG", quality=calidad, optimize=True)
                print(f"Imagen optimizada: {nombre_salida} (guardada en img/)")

# Llamar a la función para optimizar las imágenes
optimizar_imagenes()