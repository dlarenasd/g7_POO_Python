from abc import ABC, abstractmethod
from producto import Producto
class Tienda(ABC):
    nombre_tienda = ""
    costo_delivery= ""
    @abstractmethod
    def ingresar_producto(self):
        pass
    @abstractmethod
    def listar_productos(self):
        pass
    @abstractmethod
    def venta_producto(self):
        pass
    
    
class Restaurant(Tienda):
    def __init__(self, nombre_tienda:str, costo_delivery:int):
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.lista_productos = []
    
    @property
    def nombre_tienda(self):
        return self.__nombre_tienda
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    def ingresar_producto(self, nombre_producto: str, precio_producto: int, stock_producto: int):
        producto = Producto(nombre_producto, precio_producto, stock_producto) #RECUERDA QUE RESTAURANT TIENE STOCK 0
        if nombre_producto in self.lista_productos:
            producto.add_stock_producto(producto.stock_producto, stock_producto)
            return "Stock actualizado"
        else:
            self.lista_productos.append(producto)
            return "Producto ingresado"
    
    def listar_productos(self):
        retorno = (":::::::::::LISTA DE PRODUCTOS:::::::::::\n")
        self.lista_productos=[
            f"{producto}" for producto in self.lista_productos
        ] 
        return f"{retorno}{"".join(self.lista_productos)}" 

    def venta_producto(self):    
        pass
    
    
""" 
class Supermercado(Tienda):
    def __init__(self, nombre_tienda:str, costo_delivery:int):
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.lista_productos = []
    
    @property
    def nombre_tienda(self):
        return self.__nombre_tienda
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    def ingresar_producto(self):
        return super().ingresar_producto()
    def listar_productos(self):
        return super().listar_productos()
    def venta_producto(self):
        return super().venta_producto()
    pass
class Farmacia(Tienda):
    def __init__(self, nombre_tienda:str, costo_delivery:int):
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.lista_productos = []
    
    @property
    def nombre_tienda(self):
        return self.__nombre_tienda
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    def ingresar_producto(self):
        return super().ingresar_producto()
    def listar_productos(self):
        return super().listar_productos()
    def venta_producto(self):
        return super().venta_producto()
    pass


"""
if __name__ == "__main__":
    domino = Restaurant("dominó",1500)
    print(domino.ingresar_producto("completo", 1200, 15))
    print(domino.ingresar_producto("completo", 1200, 15))
    print(domino.ingresar_producto("dinámico", 1200, 15))
    print(domino.ingresar_producto("italiano", 1500, 15))
    print(domino.listar_productos())
    
