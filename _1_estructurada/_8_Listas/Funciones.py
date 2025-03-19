if __name__ == '__main__':

    #Añade un elemento  al final de la lista

    mi_lista =[1, 2, 3]
    mi_lista.append(4)
    print(mi_lista)

    #Añade los elementos a otra lista
    mi_lista = [1, 2, 3]
    otra_lista = [4, 5, 6]
    mi_lista.extend(otra_lista)
    print(mi_lista)

    #Inserta un elemento  en una posicion especial
    mi_lista = [1, 2, 3]
    mi_lista.insert(1,4)
    print(mi_lista)

    #Eliina el primer el elemento de la lista
    mi_lista =[1, 2, 3, 2]
    mi_lista.remove(2)
    print(mi_lista)

    #Elimina y devuelve el elemento en una posicion
    mi_lista = [1, 2, 3]
    elemento = mi_lista.pop(1)
    print(elemento)
    print(mi_lista)

    #Devuelve el indice de la primera aparicion
    mi_lista = [1, 2, 3, 2]
    indice = mi_lista.index(2)
    print(indice)

    #Devuele el numero de veces que aparece un numero de ocucrrencias que sale el2
    mi_lista = [1, 2, 3, 2, 2]
    conteo = mi_lista.count(2)
    print(conteo)

    #Ordena los elementos de una lista
    mi_lista = [3, 1, 4, 2]
    mi_lista.sort() #ordena de manera acendente
    print(mi_lista)
    #Ordena los elementos de una lista de manera acendete (invierte el orden)
    mi_lista.sort(reverse=True) #ordena de manera desendente
    print(mi_lista)

    #Elimina todos los elementos de la lista
    mi_lista = [1, 2, 3]
    mi_lista.clear()
    print(mi_lista)

    #Devuelve una copia de la lista
    mi_lista = [1, 2, 3]
    mi_lista2=mi_lista
    copia_lista = mi_lista.copy()
    mi_lista.append(4)
    print(copia_lista)

    """
    print("Copia")
    print(copia_lista)
    print("lista real:")
    print(mi_lista)
    """





