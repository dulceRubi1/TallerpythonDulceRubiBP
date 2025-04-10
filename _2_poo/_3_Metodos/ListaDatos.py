class ListaDatos:

    def __init__(self, matricula:str, estudiante:str, asignatura:str):
        self.matricula=matricula
        self.estudiante=estudiante
        self.asignatura=asignatura


if __name__ == '__main__':
    lista=[]
    lista.append(ListaDatos("22240021", "Dulce Rubi Barragan", "eSPAÑOL"))
    lista.append(ListaDatos("22240091", "Martin Marquez", "eSPAÑOL"))
    lista.append(ListaDatos("22240051", "Michelle Barragan  ", "eSPAÑOL"))

    for obj in lista:
        print(f"Matricula: {obj.matricula}")
        print(f"Nombre: {obj.estudiante}")
        print(f"Asigantura: {obj.asignatura}")
        print("------------------------------------")