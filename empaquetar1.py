import os

def consolidar_proyecto(directorio, archivo_salida):
    # Carpetas estándar a ignorar en proyectos Reflex y Python
    ignorar_carpetas = [
        '.git', 'venv', '.venv', '__pycache__', 
        '.web', '.states', 'node_modules', '.reflex',
        'build', 'dist'
    ]
    
    # Extensiones de archivos binarios o irrelevantes para el contexto
    ignorar_extensiones = [
        '.pyc', '.sqlite3', '.db', '.whl', '.pkl',
        '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.webp',
        '.pdf', '.zip', '.tar', '.gz', '.log'
    ]

    with open(archivo_salida, 'w', encoding='utf-8') as f_out:
        for raiz, directorios, archivos in os.walk(directorio):
            # Filtramos las carpetas a ignorar
            directorios[:] = [d for d in directorios if d not in ignorar_carpetas]
            
            for archivo in archivos:
                # Ignorar extensiones, el propio script y el archivo de salida
                if (any(archivo.lower().endswith(ext) for ext in ignorar_extensiones) or 
                    archivo == 'empaquetar.py' or 
                    archivo == archivo_salida):
                    continue
                
                ruta_completa = os.path.join(raiz, archivo)
                
                # Agregamos separadores claros
                f_out.write(f"\n{'='*50}\n")
                f_out.write(f"ARCHIVO: {ruta_completa}\n")
                f_out.write(f"{'='*50}\n")
                
                try:
                    with open(ruta_completa, 'r', encoding='utf-8') as f_in:
                        f_out.write(f_in.read() + "\n")
                except Exception:
                    f_out.write(f"[Archivo no legible como texto plano]\n")

if __name__ == '__main__':
    nombre_salida = 'contexto_proyecto.txt'
    consolidar_proyecto('.', nombre_salida)
    print(f"¡Archivo {nombre_salida} generado con éxito!")