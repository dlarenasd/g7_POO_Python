class Error(Exception): #corrección de clase// permite generar más errores derivados de esta clase
    pass

class DimensionError(Error):
    def __init__(self, mensaje:str, dimension=None, maximo=None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self): #sobrecarga del método __str__ para generar mensajes de error
        if self.dimension is None and self.maximo is None: #error cuando no están todos los datos.
            return super().__str__()
        else: #corrección de clase: inclusión de elementos si es que son necesarios
            retorno = self.mensaje
            if self.dimension:
                retorno += f"La dimensión ingresada es {self.dimension}"
            if self.maximo:
                retorno += f" y el máximo es {self.maximo}"
            return retorno

            
    
if __name__ == "__main__":
    foto1 = DimensionError("ERROR Dimensión Inválida") #ERROR Dimensión Inválida
    foto2 = DimensionError("ERROR Dimensión Inválida",2800, 2500) #ERROR Dimensión Inválida La dimensión ingresada es: 2800 y el máximo es: 2500.
    foto3 = DimensionError("ERROR Dimensión Inválida",-50,2500) #ERROR Dimensión Inválida La dimensión ingresada es: -50 y el máximo es: 2500.
    print(foto1)
    print(foto2)
    print(foto3)

    