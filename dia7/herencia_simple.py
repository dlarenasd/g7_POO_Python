class Padre():
    #atributo de clase
    color = "verde"
    #constructor
    def __init__(self, tamanio:int):
        #atributo de instancia
        self.__tamanio = tamanio  #atributo oculto/privado
        
    #métodos estáticos
    
    #métodos de instancia
    def cambia_color(self, color:str):
        if color != "":
            self.color = color
    #sobrecarga
    def __str__(self) -> str:
        return f"El color es {self.color} y el tamaño es {self.tamanio}"
    #getter y setter
    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self, tamanio:int):
        if tamanio > 0:
            self.__tamanio = tamanio
        else: 
            self.__tamanio = 0

#HERENCIA ----> SE HEREDA TODO, y cada uno de sus hijos puede tener sus propios métodos y atributos          
class Hija(Padre):
    peso = 60

class Hijo(Padre):
    deuda = 120
class Nieto(Hija): #HEREDA TODO LO DE PADRE Y LO DE HIJA
    pañal = "XL"


#instancia de la clase Hija (creando un objeto)
hijita = Hija(160)
print(f"El color de la clase hija es {hijita.color}")
print(f"Para hijita: {hijita}")
print(hijita.tamanio)
hijita.cambia_color("azul")
print(f"El color de la clase hija es {hijita.color}")
print("")
regalon = Nieto(50)
regalon.cambia_color("naranjo")
print(f"Para el regalón: {regalon}")

#print(hijita.pañal) AttributeError: 'Hija' object has no attribute 'pañal'---> LA HERENCIA ES UNIDIRECCIONAL
