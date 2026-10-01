class Libro:
    """
    Representa un libro dentro del sistema de la biblioteca.
    """
    def __init__(self, id_libro: int, titulo: str, autor: str, disponible: bool = True):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def prestar(self) -> bool:
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self) -> None:
        self.disponible = True

    def a_diccionario(self) -> dict:
        return {
            "id_libro": self.id_libro,
            "titulo": self.titulo,
            "autor": self.autor,
            "disponible": self.disponible
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            id_libro=datos["id_libro"],
            titulo=datos["titulo"],
            autor=datos["autor"],
            disponible=datos["disponible"]
        )