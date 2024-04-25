class Error(Exception): #error base para heredar exception
    pass

class LargoExcedidoError(Error):
    pass

class SubTipoInvalidoError(Error):
    pass

""" 
Yo los prefería así, pero según el diagrama están vacíos

class LargoExcedidoError(Error):#primer error específico del programa
    def __init__(self, mensaje, largo:int, limite:int): #recibe un mensaje, un largo y un límite
        self.mensaje = mensaje
        self.largo = largo
        self.limite = limite
    def __str__(self) -> str:
        return f"{self.mensaje} Ingresó {self.largo} caracteres y el límite es {self.limite}." #retorna un mensaje usando los atributos
    
class SubTipoInvalidoError(Error): #segundo error específico del programa
    def __init__(self, mensaje, tipos_disponibles): #toma como parámetro un mensaje y una variable con los tipos disponibles
        self.mensaje = mensaje
        self.tipos_disponibles = tipos_disponibles
    def __str__(self) -> str:
        return f"{self.mensaje}. Los sub-tipos disponibles son {self.tipos_disponibles}" # retorna un mensaje usando los atributos 

"""
