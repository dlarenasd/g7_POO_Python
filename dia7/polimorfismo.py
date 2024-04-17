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
    #polimorfismo es un cambio en el comportamiento del método
    def cambia_color(self, color:str):
        #if color != "":  cambio en el comportamiento, según como estaba escrito
            self.color = color

class Hijo(Padre):
    deuda = 120
    #sobreescribir el constructor
    def __init__(self, tamanio: int, saldo = 0):
        super().__init__(tamanio) #llamado al constructor del padre
        self.__saldo = saldo
    @property #getter para el atributo privado
    def saldo(self):
        return self.__saldo
class Nieto(Hija): #HEREDA TODO LO DE PADRE Y LO DE HIJA
    pañal = "XL"


#instancia de la clase Hija (creando un objeto)
hijita = Hija(160)
print(f"El color de la clase hija es {hijita.color}")
print(f"Para hijita: {hijita}")
print(hijita.tamanio)
hijita.cambia_color("")
print(f"El color de la clase hija es {hijita.color}")
print("")
regalon = Nieto(50)
regalon.cambia_color("naranjo")
print(f"Para el regalón: {regalon}")

#print(hijita.pañal) AttributeError: 'Hija' object has no attribute 'pañal'---> LA HERENCIA ES UNIDIRECCIONAL

super(type(hijita),hijita).cambia_color("gris") #llamado al método del padre a través de la hija, afectando atributos de la instancia de clase hija
print(f"El color de la clase hija es {hijita.color}")
#instancia de clase Hijo
hijito = Hijo(167, 1200)
print(f"El tamaño es: {hijito.tamanio} y su saldo es: {hijito.saldo}")

print(f"hijita es instancia de Hija: {isinstance(hijita,Hija)}") #True
print(f"hijita es instancia de Hijo: {isinstance(hijita,Hijo)}") #False
print(f"hijita es instancia de Padre: {isinstance(hijita,Padre)}") #True
print(f"hijita es instancia de Nieto: {isinstance(hijita,Nieto)}") #False
print(f"hijito es instancia de Hijo: {isinstance(hijito,Hijo)}") #True
print(f"hijito es instancia de Hija: {isinstance(hijito,Hija)}") #False
print(f"hijito es instancia de Padre: {isinstance(hijito,Padre)}") #True
print(f"regalón es instancia de Hija: {isinstance(regalon,Hija)}") #True
print(f"regalón es instancia de Hijo: {isinstance(regalon,Hijo)}") #False
print(f"regalón es instancia de Padre: {isinstance(regalon,Padre)}") #True