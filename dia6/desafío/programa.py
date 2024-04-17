from tienda import Tienda, Restaurant, Supermercado, Farmacia
from producto import Producto

print("::::::::::BIENVENIDO A TU TIENDA:::::::::: ")

continuar = "s"
mostrar_opciones = 1
lista_opciones = [1,2,3]

nombre_tienda = input("¿Qué nombre tendrá tu tienda?\n")
costo_delivery = int(input("Cuál será el costo de delivery?\n"))
tipo_tienda = int(input("""¡Excelente! ¿Qué tipo de tienda le gustaría crear?
                        1. Restaurant
                        2. Supermercado
                        3. Farmacia \n"""))
if tipo_tienda == 1:
    t = Restaurant(nombre_tienda,costo_delivery)
elif tipo_tienda == 2:
    t = Supermercado(nombre_tienda, costo_delivery)
elif tipo_tienda == 3:
    t = Farmacia(nombre_tienda, costo_delivery)
else: 
    print("Error de ingreso de datos")
    exit()

print("Pasemos al ingreso de productos")
if isinstance(t,Restaurant):
    while continuar == "s":
        nombre = input("Ingrese el nombre del producto \n")
        precio = int(input("Ingrese el precio del producto \n"))
        t.ingresar_producto(nombre, precio)
        continuar = input("¿Desea seguir agregando productos? [s/n]\n")
        if continuar != "s" and continuar != "n":
            print("Ingreso de comando inválido")
else:
    while continuar == "s":
        nombre = input("Ingrese el nombre del producto \n")
        precio = int(input("Ingrese el precio del producto \n"))
        stock = int(input("Ingrese el stock del producto \n"))
        t.ingresar_producto(nombre, precio, stock)
        continuar = input("¿Desea seguir agregando productos? [s/n]\n")
        if continuar != "s" and continuar != "n":
            print("Ingreso de comando inválido")

continuar = "s"

while mostrar_opciones < 3:
    mostrar_opciones = int(input(""" ¿Qué desea hacer a continuación?
                                1. Listar productos existentes
                                2. Realizar una venta
                                3. Salir del programa \n"""))
    if mostrar_opciones == 1:
        print(t.listar_productos())
        
    elif mostrar_opciones == 2:
        while continuar == "s":
            venta_nombre = input("Ingrese el nombre del producto que va a vender \n")
            cantidad = int(input("¿Cuántos va a vender? \n"))
            print(t.venta_producto(venta_nombre, cantidad))
            continuar = input("¿Desea continuar vendiendo productos? [s/n] \n")
    elif mostrar_opciones == 3:
        print("¡Nos vemos a la próxima!")
    else:
        print("Ingreso de operación inválida")

print("Fin del programa")

        