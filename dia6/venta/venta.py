class DetalleVentaItem():
    def __init__(self, producto: str, cantidad: int):
        self.__producto = producto
        self.__cantidad = cantidad
    @property
    def producto(self): #getter
        return self.__producto
    @property
    def cantidad(self): #getter
        return self.__cantidad

class DetalleVenta():
    def __init__(self):
        self.__items = [] #constructor para hacer una lista vacía
    def agregar_item(self, item: DetalleVentaItem): #
        self.__items.append(item)
    def __str__(self):
        retorno = (":::::::: DETALLE DE ESTA VENTA :::::::::\n" "PRODUCTO\tCANTIDAD\n")
        items = [
            f"{i.producto}\t\t{i.cantidad}\n" for i in self.__items
        ]
        return f"{retorno}{''.join(items)}"

class Venta():
    def __init__(self): #composición
        self.__detalle = DetalleVenta()
    
    def modificar_detalle(self, detalle_venta_item : DetalleVentaItem ):
        #agregación
        self.__detalle.agregar_item(detalle_venta_item)
    @property
    def detalle(self):
        return self.__detalle