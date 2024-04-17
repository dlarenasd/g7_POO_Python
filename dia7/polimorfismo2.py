class Madre():
    def __init__(self, color:str, **kwargs):
        super().__init__(**kwargs)    
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color:str):
        self.__color = color
        
class Padre():
    def __init__(self, tamanio:int, **kwargs):
        super().__init__(**kwargs)    
        self.__tamanio = tamanio
    
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio:int):
        self.__tamanio = tamanio
        
class Hija(Madre,Padre): #Con este orden el constructor vigente es el de la Madre, al instanciarla pedirá color. Si fuese Padre primero, 
                    #la instacia pediría que se le ingrese un tamanio. MRO: Method Resolution Order
    """  #sobreescritura de constructores
    def __init__(self, color: str, tamanio:int):
        Madre.__init__(self, color)
        Padre.__init__(self, tamanio)"""
    def __init__(self, deuda = 0, **kwargs):
        super().__init__(**kwargs)        

        #atributo de instancia propio de hija
        self.deuda = deuda

class Nieto(Hija):
    pañal="XL"
    
""" 
princesa = Hija("Morado",90)
#print(princesa.tamanio) # AttributeError: 'Hija' object has no attribute '_Padre__tamanio'
#princesa.tamanio = 90 #a través del setter, genero el atributo que no existe y le asigno un valor
print(princesa.tamanio) #post setter se puede solicitar este dato sin error
print(f"El color de la clase hija es {princesa.color}")
print(f"Para princesa el tamaño es {princesa.tamanio} cm")
"""
princesa = Hija(deuda=350, color="azul", tamanio=100)
print(princesa.deuda, princesa.color, princesa.tamanio) #350 azul 100
guaguito = Nieto(deuda=0, color="celeste", tamanio= 20)

#ISINSTANCE: PRIMERO EL OBJETO Y LUEGO LA CLASE A COMPARAR isinstance(objeto,Clase)
print(f"princesa es instancia de Hija: {isinstance(princesa,Hija)}") #True
print(f"princesa es instancia de Padre: {isinstance(princesa,Padre)}") #True
print(f"princesa es instancia de Madre: {isinstance(princesa,Madre)}") #True
print("")
print(f"guaguito es instancia de Hija: {isinstance(guaguito,Hija)}") #True
print(f"guaguito es instancia de Padre: {isinstance(guaguito,Padre)}") #True
print(f"guaguito es instancia de Madre: {isinstance(guaguito,Madre)}") #True