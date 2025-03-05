if __name__ == '__main__':
    nombre1 = input("dame  el primer nombre: ")
    nombre2 = input("Damwe el segundo nombre: ")

    t1=len (nombre1 )
    t2=len(nombre2)
    if t1==t2:
        print(f"los nombres {nombre1} y {nombre2} son iguales")
    else:
       if t1>t2:
        print(f"el nombre mas grande es {nombre1} por {t1} letras ")
       else:
          if t2>t1:
            print(f"el nombre mas grande es {nombre2} por  {t2} lwtras ")















