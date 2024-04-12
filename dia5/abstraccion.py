""" 
ABSTRACCIÓN: 
Una clase es abstracta si tiene, a lo menos, un método abstracto.
Un método abstracto: Son aquellos que solamente tienen la definición del método,
además debe tener el decorador @abstractmethod

Para poder crear una clase abstracta y un método abstracto vamos a tener que importar:

from abc import ABC, abstractmethod

al crear una clase se agrega el ABC dentro de los paréntesis de la clase
"""
from abc import ABC, abstractmethod

class Pelota(ABC):
    
    #definición de método abstracto
    @abstractmethod
    def rebotar(self, altura:int):
        pass
    
#creación de una sub-clase--> una clase que nace a partir de otra clase
class PelotaDeJuguete(Pelota):
    def __init__(self):
        self.color = "Blanco"
    
    #obligación de implementar el método abstracto
    def rebotar(self, altura:int):
        pass
#creación de objeto
pelotita = PelotaDeJuguete()
print(pelotita.rebotar(20))