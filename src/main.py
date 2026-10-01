from src.models import Libro
from src.storage import GestorAlmacenamiento

def mostrar_menu():
    print("\n--- 📚 SISTEMA DE GESTIÓN DE BIBLIOTECA ---")
    print("1. Agregar un libro")
    print("2. Listar todos los libros")
    print("3. Prestar un libro")
    print("4. Devolver un libro")
    print("5. Salir")

def main():
    storage = GestorAlmacenamiento()
    libros = storage.cargar_libros()

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ").strip()

        if opcion == "1":
            try:
                id_libro = int(input("Ingrese el ID del libro (número): "))
                # Verificar si el ID ya existe
                if any(l.id_libro == id_libro for l in libros):
                    print("❌ Error: Ya existe un libro con ese ID.")
                    continue
                titulo = input("Ingrese el título: ").strip()
                autor = input("Ingrese el autor: ").strip()
                
                nuevo_libro = Libro(id_libro, titulo, autor)
                libros.append(nuevo_libro)
                storage.guardar_libros(libros)
                print(f"✅ Libro '{titulo}' agregado exitosamente.")
            except ValueError:
                print("❌ Error: El ID debe ser un número entero válido.")

        elif opcion == "2":
            if not libros:
                print("\n📭 No hay libros registrados en la biblioteca.")
            else:
                print("\n--- CATÁLOGO DE LIBROS ---")
                for libro in libros:
                    estado = "🟢 Disponible" if libro.disponible else "🔴 Prestado"
                    print(f"[{libro.id_libro}] {libro.titulo} - {libro.autor} | Estado: {estado}")

        elif opcion == "3":
            try:
                id_libro = int(input("Ingrese el ID del libro a prestar: "))
                libro_encontrado = next((l for l in libros if l.id_libro == id_libro), None)
                
                if libro_encontrado:
                    if libro_encontrado.prestar():
                        storage.guardar_libros(libros)
                        print(f"✅ Has pedido prestado '{libro_encontrado.titulo}'.")
                    else:
                        print("⚠️ El libro ya se encuentra prestado.")
                else:
                    print("❌ No se encontró ningún libro con ese ID.")
            except ValueError:
                print("❌ Error: Por favor ingresa un ID numérico.")

        elif opcion == "4":
            try:
                id_libro = int(input("Ingrese el ID del libro a devolver: "))
                libro_encontrado = next((l for l in libros if l.id_libro == id_libro), None)

                if libro_encontrado:
                    libro_encontrado.devolver()
                    storage.guardar_libros(libros)
                    print(f"✅ El libro '{libro_encontrado.titulo}' ha sido devuelto.")
                else:
                    print("❌ No se encontró ningún libro con ese ID.")
            except ValueError:
                print("❌ Error: Por favor ingresa un ID numérico.")

        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el sistema de biblioteca! Hasta luego.")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()