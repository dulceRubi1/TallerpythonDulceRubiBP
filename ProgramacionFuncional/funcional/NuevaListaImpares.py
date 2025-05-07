if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    listaPares=list(filter(lambda  x: x%2==0,numeros))
    listaImpares=list(filter(lambda  x: x%2==1,numeros))

    print(f"lista de numeros pares: {listaPares}")
    print(f"lista de numeros impares: {listaImpares}")

    ListaImparesConPotencia=list(map(lambda z:z**2,filter(lambda t: t%2==1,numeros)))
    #print(f"Numeros cuadrdaos de una lista: {list(map(lambda x: x ** 2, numeros ))}")
