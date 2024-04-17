class Producto():
    def __init__(self, nombre_producto: str, precio_producto:int, stock_producto = 0):
        self.__nombre_producto = nombre_producto
        self.__precio_producto = precio_producto
        self.__stock_producto = stock_producto if stock_producto > 0 else 0

    @property
    def nombre_producto(self):
        return self.__nombre_producto
    @property
    def precio_producto(self):
        return self.__precio_producto
    
    @property
    def stock_producto(self):
        if self.__stock_producto == 0:
            return ""
        return self.__stock_producto
    @stock_producto.setter
    def stock_producto(self, stock_producto):
        self.__stock_producto = stock_producto
        
    def __eq__(self, other):
        return self.nombre_producto == other.nombre_producto
    
    def __iadd__(self, other):
        if self == other:
            self.__stock_producto += other.stock_producto
        return self
    
    def __sub__(self, other):
        if self == other:
            self.__stock_producto -= other.stock_producto
        return self

    def __str__(self):
        if self.__stock_producto <=10 and self.__stock_producto > 0:
            return f"{self.nombre_producto}\t\t{self.precio_producto}\t\t{self.stock_producto} Pocos productos disponibles\n"
        return f"{self.nombre_producto}\t\t {self.precio_producto}\t\t{self.stock_producto}\n"
