class Hospital:
    def __init__(self):
        self.__Nombrepaciente:str="federico"
        self.__nss:int=1258
        self.__enfermedad:str=""

    def getNombrePaciente(self)->str:
        return self.__Nombrepaciente

    def getNss(self)->int:
        return self.__nss

    @property #ESto convierte el estado en una proiedad de solo lectura

    def getEnfermedad(self)->str:
        return self.__enfermedad

    def setNombrePaciente(self, nombre:str):
        self.NombrePaciente=nombre

    def setNss(self, nss:int):
        self.nss=nss

    #@dosis_hora.setter #Esto convierte el metodo en una propiedad de solo lectura
    def setEfermedad(self, enfermedad= str):
        self.enfermedad=enfermedad


if __name__ == '__main__':
    hospital=Hospital()

    hospital.__NombrePaciente="Juan"
    print(hospital.getNombrePaciente())

