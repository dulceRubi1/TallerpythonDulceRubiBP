import random


def adivina_el_numero():

    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10

    print("¡Bienvenido a Adivina el Numero!")
    print("Estoy pensado en un número entre 1 y 100")
    print("Adivina el numero")


    while intentos < max_intentos:
        try:

            intento = int(input(f"\nIntento #{intentos + 1} - Ingresa un número: "))

            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número entre 1 y 100: ")
                continue


            intentos += 1

            if intento < numero_secreto:
                print("¡El numero es mayor! Intenta de nuevo: ")
            elif intento > numero_secreto:
                print("¡El númeroes menor! Intenta de nuevo: ")
            else:
                print(f"¡Lo lograste! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido: ")

    if intentos == max_intentos and intento != numero_secreto:
        print(f"\n Suerte para la proxima, no lograste adivinar el número")
        print(f" El número es: {numero_secreto}.")
        print("¡Gracias por jugar!")


adivina_el_numero()

"""
Lider: Elsi Abril Mendez Escalante
Dulce Rubi Barragan Peñaloza

"""