class Madre():
    def __init__(self, color:str):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color:str):
        self.__color = color
        
class Padre():
    def __init__(self, tamanio:int):
        self.__tamanio = tamanio
    
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio:int):
        self.__tamanio = tamanio
        
class Hija(Madre,Padre): #Con este orden el constructor vigente es el de la Madre, al instanciarla pedirá color. Si fuese Padre primero, 
    pass                #la instacia pediría que se le ingrese un tamanio.

princesa = Hija("Morado")
#print(princesa.tamanio) # AttributeError: 'Hija' object has no attribute '_Padre__tamanio'
princesa.tamanio = 90 #a través del setter, genero el atributo que no existe y le asigno un valor
print(princesa.tamanio) #post setter se puede solicitar este dato sin error