
import json
from pathlib import Path


def leer_json(ruta_archivo):
    """
    Lee un archivo JSON y devuelve su contenido como estructura de Python.

    :param ruta_archivo: Ruta del archivo JSON a leer.
    :return: contenido del JSON en formato Python (lista o diccionario).
    """
    try:
        # Path facilita el manejo de rutas y hace el código más legible
        path = Path(ruta_archivo)

        with path.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_archivo}")
        return []
    except json.JSONDecodeError:
        print(f"El archivo no tiene un JSON válido: {ruta_archivo}")
        return []
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []
