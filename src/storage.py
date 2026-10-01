import json
import os
from src.models import Libro

class GestorAlmacenamiento:
    """
    Maneja la lectura y escritura de libros en el archivo JSON.
    """
    def __init__(self, ruta_archivo: str = "data/biblioteca.json"):
        self.ruta_archivo = ruta_archivo

    def guardar_libros(self, libros: list[Libro]) -> None:
        datos = [libro.a_diccionario() for libro in libros]
        os.makedirs(os.path.dirname(self.ruta_archivo), exist_ok=True)
        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar_libros(self) -> list[Libro]:
        if not os.path.exists(self.ruta_archivo):
            return []
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return [Libro.desde_diccionario(item) for item in datos]
        except (json.JSONDecodeError, FileNotFoundError):
            return []