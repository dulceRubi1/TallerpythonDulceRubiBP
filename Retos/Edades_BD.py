import json
import sys


def iterador():
    with open("Edades.Json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    for Personas in datos["usuariosbd"]:
        yield (Personas["id"], Personas["Nombre"], Personas["Edad"], Personas["RFC"])


if __name__ == '__main__':
    # Definición de códigos ANSI
    RESET = "\033[0m"  # Restablece el color a su valor por defecto
    # Colores de texto
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    # Colores de fondo
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    i=5
    for id, Nombre, Edad, RFC in iterador():
        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(GREEN)
            case 3:
                sys.stdout.write(BLUE)
            case 4:
                sys.stdout.write(WHITE)
            case 5:
                sys.stdout.write(MAGENTA)
            case _:
                sys.stdout.write(RESET)




        print(" Persona con la ID: ", id)
        print("usuario:", id)
        print("-----------------------------")
        print("Id: ", id)
        print("-----------------------------")
        print("Nombre: ", Nombre)
        print("-----------------------------")
        print("Edad: ", Edad)
        print("-----------------------------")
        print("RFC: ", RFC)
        print("-----------------------------")

        if Edad >= 18:
            print(f"Es mayor de edad")
        else:
            print(f"Es menor de edad ")
        print("")
        print("")
i=5







