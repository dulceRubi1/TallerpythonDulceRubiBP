class Datos:
    def __init__(self, nombre, correo, whatsap):
        self.nombre = nombre
        self.correo = correo
        self.whatsap = whatsap


    def setNombre(self, nombre:str):
        self.nombre=nombre


if __name__ == '__main__':
    datos=Datos('Dulce', 'dulcerubi1214pe@gmail.com', '2481338690')

    print(datos.nombre)
    datos.setNombre("Rubi")
    print(datos.nombre)
    datos.nombre="Dulce"
    print(datos.nombre)



    