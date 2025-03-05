if __name__ == '__main__':
    a: int = 50
    b: int = 100
    c: int = 50
    d: int = 50
    e: int = 100


    if a==b and c==d:
        print(f"Los valores de {a}, {c}, {d} son iguales")
    elif b+e<a+c+d:
        print(f"La suma de b + e ({b + e}) es menor que la suma de a + c + d ({a + c + d})")
    elif a+b+c+d>e:
        print(f"La suma de a + b + c + d ({a+b+c+d}) es mayor que e ({e})")
    elif a>b and c<d:
        print(f"a ({a}) es mayor que b ({b}) y c ({c}) es menor que d ({d})")
    elif a+b+c==e:
        print(f"La suma de a + b + c ({a+b+c}) es igual a e ({e})")
    else:
        print("n")

