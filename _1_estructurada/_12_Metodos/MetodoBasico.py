import statistics as Dulce

#def suma(a:int, b:int):
    #print(f"La suma de {a} + {b} es {a+b}")

def suma(a:int, b=None, c=None):

    if b is None:
        print(f"{a} ")
    elif c is None:
        print(f"La suma de {a} + {b} es {a+b} ")
    else:
        print(f"La suma de {a} + {b} + {c} es {a+b+c} ")

def promedioArreglo(lista):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p=Dulce.mean(lista)
    print(f"el promedio es {p}")


if __name__ == '__main__':

    #suma(10)
    #suma(10)
    #suma(10)

    #suma(10, 19)
    #suma(10, 20)
    #suma(10, 21)

    suma(10, 52, )
    suma(23, 47, 50)
    suma(12)

    lista2=[1,2,3,4,5]
    promedioArreglo(lista2)
    print(lista2)

#La lista saldra del metodo de modo alterada
