from distutils.msvc9compiler import query_vcvarsall

if __name__ == '__main__':
    palabra: str = "%s"
    lista: list = ["nombre", "Apellido_Patero", "nombre_usuario", "edad","correo electronico","contraseña"]

    print(palabra)
    #palabra=palabra * 5
    print(palabra)

    t=len(lista) #obtiene el total de elementos de un alista
    print(t)

    palabra=palabra * len(lista)
    print(palabra)

    campos=" , ".join(lista)#
    print(campos)

    querySQL = " , ".join(lista)#
    print(campos)

    querySQL= f"INSERT INTO tabla ({campos}) VALUES ({palabra}) "
    print(querySQL)
