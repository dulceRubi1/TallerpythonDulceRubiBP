import sys


import sys
if __name__ == '__main__':
    print("rango de 0 a 9")
    for i in range(10):
        print(F"{i}")

    print("rango de 6 a 11")
    for i in range(6,12):
            print(F"{i}")

    print("rango de 6 a 9 pero con incrementos de 3")
    for i in range(6,12,3):
     print(F"{i}")

    print("-------------------")
    for j in range(1,20):
        print(f"{j}", end=" ")

    sys.stdout.write("Texto sin salto de linea")

    print("----------------------------")
    lista=[1,2,3,"Lunes",4,5,6,7,8,9,10,11,12,13,14,15,16]

    lista.append(200)
    lista.append("Viernes")
    lista.append(False)
    lista.append(2.69)

    Lista2=[1200,1300,1500]

    lista.append(Lista2)

    for elemento in lista:
        print(elemento)

    Lista2=[17,18,19,20]
    lista.extend(Lista2)

    nombre:str
    nombre="Luis"
    nombre +=" Gutierrez"
    nombre.join("Gutierrez")
    print(nombre)

    Lista3 = ["Federico", "Pablo", "Karla"]
    cadena:str=" - ".join(Lista3)
    print(cadena)

    separado=cadena.split()
    for dato in separado:
      print(dato)
