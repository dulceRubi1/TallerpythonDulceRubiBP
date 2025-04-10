class ListaDatos:
    def __init__(self,matriula:str,estudiante:str,asignatura:str):
        self.matricula= matriula
        self.estudiante= estudiante
        self.asignatura= asignatura

class ControlEscolar:

    def __init__(self):
        self.lista=[]

    def addEstudiante(self,matricula,estudiante,asignatura):
        self.lista.append(ListaDatos(matricula,estudiante,asignatura))

    def show(self):
        for obj in self.lista:
            print(f"estudiante:{obj.estudiante}")
            print(f"matricula:{obj.matricula}")
            print(f"asignatura:{obj.asignatura}")
            print("---------------------------------------")

if __name__ == '__main__':
    escolar=ControlEscolar()
    escolar.addEstudiante("22240057", "Alison Alonso", "Estructura de Datos")
    escolar.addEstudiante("22240041", "Alfredo Morales", "POO")
    escolar.addEstudiante("22240059", "Elsi Mendez", "POO")
    escolar.addEstudiante("22240001", "Dulce Barragan", "Estructura de Datos")
    escolar.addEstudiante("22240060", "Tomas Diaz", "POO")

    escolar.show()

    