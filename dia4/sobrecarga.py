class Auto():
    def __init__(self, color: str = "blanco" ):
        self.__color = color
    
    def __str__(self):
        return f"Método sobrecargado {self.__color}"    
    
nissan = Auto()
print(nissan) #<__main__.Auto object at 0x0000025C9F799CD0> --> "es una instancia de la clase Auto()"
# luego de hacer la sobrecarga de método __str__ el output es : Método sobrecargado

raize = Auto("Celeste")
print(raize)