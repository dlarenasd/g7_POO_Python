class DimensionError(Exception):
    def __init__(self, mensaje=str, dimension=None, maximo=None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self):
        if self.dimension <= 0:
            return f"{self.mensaje} La dimensión ingresada es: {self.dimension} y el mínimo es: 1."
        elif self.dimension is not None and self.maximo is not None:
            return f"{self.mensaje} La dimensión ingresada es: {self.dimension} y el máximo es: {self.maximo}."
        else:
            return super().__str__()
            
    
if __name__ == "__main__":
    foto1 = DimensionError("ERROR Dimensión Inválida")
    foto2 = DimensionError("ERROR Dimensión Inválida",2800, 2500)
    foto3 = DimensionError("ERROR Dimensión Inválida",-50,2500)
    print(foto1)
    print(foto2)
    print(foto3)

    