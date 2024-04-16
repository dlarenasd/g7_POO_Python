class Producto():
    def __init__(self, nombre_producto: str, precio_producto:int, stock_producto = 0):
        self.__nombre_producto = nombre_producto
        self.__precio_producto = precio_producto
        self.__stock_producto = stock_producto
        if self.stock_producto < 0:
            stock_producto = 0
    

    @property
    def nombre_producto(self):
        return self.__nombre_producto
    @property
    def precio_producto(self):
        return self.__precio_producto
    
    @property
    def stock_producto(self):
        return self.__stock_producto
        
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
        return f"Nombre: {self.nombre_producto} \t Precio: {self.precio_producto}\t Stock: {self.stock_producto}\n"