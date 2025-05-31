from PIL import Image
import os
import shutil

for root, dirs, files in os.walk("."):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            ruta_original = os.path.join(root, file)
            ruta_webp = os.path.splitext(ruta_original)[0] + ".webp"
            nombre_archivo = os.path.basename(ruta_original)

            if not os.path.exists(ruta_webp):
                try:
                    img = Image.open(ruta_original).convert("RGB")
                    img.save(ruta_webp, "webp", quality=90)
                    print(f"✔️  {ruta_webp} creado")

                    # Crear carpeta 'anteriores' si no existe
                    carpeta_anteriores = os.path.join(root, "anteriores")
                    os.makedirs(carpeta_anteriores, exist_ok=True)

                    # Mover archivo original
                    ruta_destino = os.path.join(carpeta_anteriores, nombre_archivo)
                    shutil.move(ruta_original, ruta_destino)
                    print(f"📁  Original movido a: {ruta_destino}")

                except Exception as e:
                    print(f"❌ Error con {ruta_original}: {e}")
            else:
                print(f"⚠️  Ya existe: {ruta_webp} (omitido)")
