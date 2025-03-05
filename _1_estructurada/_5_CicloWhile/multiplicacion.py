if __name__ == '__main__':
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa segundo número: "))

    r = 0
    i = 0
    while i < y:
        r += x
        i += 1
    print(f"el resultado de {x} * {y} es igual {r}")