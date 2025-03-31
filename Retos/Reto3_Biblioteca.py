class Biblioteca:
    def _init_(self):

        self.libros = []
        self.usuarios = {}

    def agregar_libro(self, titu, autor, gen, copias):
        """ Agrega un libro al sistema """
        libro = {'titulo': titu, 'autor': autor, 'genero': gen, 'copias': copias}
        self.libros.append(libro)
        print(f"El libro '{titu}' ha sido agregado.")

    def buscar_libro(self, criterio):
        """ Busca libros por título, autor o género """
        res = []
        for libro in self.libros:
            if criterio in libro['titulo'].lower() or criterio in libro['autor'].lower() or criterio in libro['genero'].lower():
                res.append(libro)
        return res

    def prestar_libro(self, usuario, titulo):
        """ Presta un libro, si hay copias disponibles """
        for libro in self.libros:
            if libro['titulo'].lower() == titulo.lower():
                if libro['copias'] > 0:
                    if usuario not in self.usuarios:
                        self.usuarios[usuario] = []
                    self.usuarios[usuario].append(libro)
                    libro['copias'] -= 1
                    print(f"Se ha prestado el libro '{titulo}' a {usuario}.")
                    return
                else:
                    print(f"No hay copias disponibles de '{titulo}'.")
                    return
        print(f"El libro '{titulo}' no está disponible en la biblioteca.")

    def devolver_libro(self, usuario, titulo):
        """ Devolver un libro prestado """
        if usuario in self.usuarios:
            for libro in self.usuarios[usuario]:
                if libro['titulo'].lower() == titulo.lower():
                    libro['copias'] += 1
                    self.usuarios[usuario].remove(libro)
                    print(f"El libro '{titulo}' ha sido devuelto por {usuario}.")
                    return
        print(f"{usuario} no tiene el libro '{titulo}'.")

    def mostrar_libros_disponibles(self):
        """ libros con copias disponibles """
        disponible = [libro for libro in self.libros if libro['copias'] > 0]
        return disponible

    def mostrar_libros(self):
        """ Muestra libros en la biblioteca """
        return self.libros

    def iterar_libros(self):
        """ Generador para recorrer los libros de manera eficiente """
        for libro in self.libros:
            yield libro

def menu(biblioteca):
    while True:
        print("\n----- Menú de Biblioteca -----")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros disponibles")
        print("6. Mostrar todos los libros")
        print("7. Salir")

        opcion = input("Elige una opción del menu: ")

        if opcion == '1':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            genero = input("Género del libro: ")
            copias = int(input("Número de copias: "))
            biblioteca.agregar_libro(titulo, autor, genero, copias)

        elif opcion == '2':
            criterio = input("Busca el Libro: ").lower()
            resultados = biblioteca.buscar_libro(criterio)
            if resultados:
                for libro in resultados:
                    print(f"{libro['titulo']} - {libro['autor']} - {libro['genero']} - Copias disponibles: {libro['copias']}")
            else:
                print("No se encontraron resultados.")

        elif opcion == '3':
            usuario = input("Nombre del usuario: ")
            titulo = input("Título del libro a prestar: ")
            biblioteca.prestar_libro(usuario, titulo)

        elif opcion == '4':
            usuario = input("Nombre del usuario: ")
            titulo = input("Título del libro a devolver: ")
            biblioteca.devolver_libro(usuario, titulo)

        elif opcion == '5':
            libros_disponibles = biblioteca.mostrar_libros_disponibles()
            if libros_disponibles:
                for libro in libros_disponibles:
                    print(f"{libro['Titulo']} - {libro['Autor']} - {libro['Genero']} - Copias disponibles: {libro['copias']}")
            else:
                print("No hay libros disponibles.")

        elif opcion == '6':
            todos_los_libros = biblioteca.mostrar_libros()
            if todos_los_libros:
                for libro in todos_los_libros:
                    print(f"{libro['Titulo']} - {libro['Autor']} - {libro['Genero']} - Copias: {libro['copias']}")
            else:
                print("No hay libros en la biblioteca.")

        elif opcion == '7':
            print("¡adiosito!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción dentro del menu.")

def main():
    biblioteca = Biblioteca()
    menu(biblioteca)

if __name__ == '__main__':
    main()