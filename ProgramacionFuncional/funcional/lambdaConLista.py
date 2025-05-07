from math import pow


#def potencia (x:int)-> int:
   # return int(pow(x,2))

if __name__ == '__main__':

    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

    print(f"Numeros originales: {numeros}")
    #print(f"la suma total con unA FUNCION  {suma(numeros)}")

    potencia = lambda x: x*x

    numerosCuadrados =list(map(lambda x: x * x, numeros))
    print(f"Mumeros cuadrdos con una funcion {numerosCuadrados}")