# Clase Libro
#Realizar un programa en python que utilice
#la POO para registrar un libro (ISBN, Titulo
# y Autor)
#Los atributos debe estar en priado
#debes tener un constuctor para el registro
#debes tener solo getters de cada atributo

#En otra clase debera registrar una coleccion
#de lirbos
#En esta clase debes tener add, delete y show

class Libro:
    def __init__(self, isbn, titulo, autor):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor

    def getisbn(self):
        return self.__isbn

    def gettitulo(self):
        return self.__titulo

    def getautor(self):
        return self.__autor

if __name__ == '__main__':
    libros=[]
    libros.append(Libro('9786071653529', "El comprador de vidas", "José Antonio del Cañizo" ))
    libros.append(Libro('7373737737', "Diario de Ana Fran", "Ana Frank" ))
    libros.append(Libro('2385283578458', "El llano en llamas", "Juan Rulfo" ))
    libros.append(Libro('999843483934', "Pedro Paramo", "Juan Rulfo" ))
    libros.append(Libro('399375943', "Diles que no me maten", "Juan Rulfo" ))

    for obj in libros:
        print(f"ISBN DE LIBRO: {obj.isbn}")
        print(f"TITULO: {obj.titulo}")
        print(f"autor : {obj.autor}")
        print("------------------------------------")


