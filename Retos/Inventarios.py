def menunuevo():
    print("\nInventario -----TIENDA TILINAS-----")
    print("A. Nuevo producto")
    print("B. Inventario")
    print("C. Vender Productos")
    print("D. Salir de -----TIENDA TILINAS----- ")


def productoN(inventario):
    nombre = input("NOMBRE DEL PRODUCTO NUEVO: ")
    cant = int(input("Cantidad de producto: "))

    for product in inventario:
        if product[0] == nombre:
            product[1] += cant
            print(f"Cantidad actualizada: {product[1]} - {product[0]} unidades")
            return

    inventario.append([nombre, cant])
    print(f"Cantidad de productos: {nombre} - {cant} unidades")


def inventariotilinas(inventario):
    if not inventario:
        print("Mo existe nada en tu inventario.")
    else:
        print("\nTu inventario es de :")
        for product in inventario:
            print(f"  {product[1]} unidades de {product[0]}")


def vproductos(inventario):
    nombre = input("PRODUCTO A VENDER : ")
    for product in inventario:
        if product[0] == nombre:
            cantidad = int(input("¿CUANTAS UNIDADES DESEAS VENDER?: "))
            if cantidad > product[1]:
                print("No hay suficiente unidades .")
                return
            product[1] -= cantidad
            print(f"VENTA EXITOSA: Se vendieron {cantidad} unidades de {nombre}")
            if product[1] == 0:
                inventario.remove(product)
                print(f"{nombre} no existe en el inventario.")
            return
    print("No existe este producto ):.")


def main():
    inventario = []
    while True:
        menunuevo()
        op = input("Seleccione una opción "" ").upper()  # Convertimos la opción a mayúscula
        if op == "A":
            productoN(inventario)
        elif op == "B":
            inventariotilinas(inventario)
        elif op == "C":
            vproductos(inventario)
        elif op == "D":
            print("Gracias por visitar -----TIENDA TLINAS------")
            break
        else:
            print("Erros, vuelve a intentar.")







if __name__ == '__main__':
    main()



"""
Lider: Elsi Abril Mendez Escalante
Dulce Rubi Barragan Peñaloza
Alison Cecilia Alnso Meneses

"""