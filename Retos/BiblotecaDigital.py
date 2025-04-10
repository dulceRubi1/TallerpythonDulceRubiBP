class ColeccionLibros:
    def _init_(self):
        self.libros = []


    def add(self, libro):
        self.libros.append(libro)


    def delete(self, isbn):
        for libro in self.libros:
            if libro.get_isbn() == isbn:
                self.libros.remove(libro)
                print(f"Libro con ISBN {isbn} eliminado.")
                return
        print(f"Libro con ISBN {isbn} no encontrado.")


    def show(self):
        if not self.libros:
            print("No hay libros en la colección.")
            return
        for libro in self.libros:
            print(f"ISBN: {libro.get_isbn()}, Título: {libro.get_titulo()}, Autor: {libro.get_autor()}")
