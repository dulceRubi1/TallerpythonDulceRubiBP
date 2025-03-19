import statistics as Dulce

if __name__ == '__main__':
    numeros=[80,80,10,30,20,20,10]

    conteo=0
    suma=0
    promedio=0
    for valor in numeros:
        suma+=valor
        conteo+=1

    promedio=suma/conteo
    print(promedio)

    #Opcion Medio Lenta
    suma=0
    for valor in numeros:
        suma+=valor
    promedio =suma/len(numeros)
    print(promedio)

    #Opcion Rapida
    promedio== Dulce.mean(numeros)
    print(promedio)


