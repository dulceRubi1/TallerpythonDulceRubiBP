if __name__ == '__main__':
    x = int(input("Ingresa un número: "))
    y = int(input("Ingresa la potencia: "))

    i:int=1
    pot:int = 1

    while i <= y:
        pot=pot* x
        i += 1

    print(f"El resultado de {x}^{y} = {pot}")
