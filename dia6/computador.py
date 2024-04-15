class Ram():
    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.byte = 32

class DiscoDuro():
    def __init__(self, capacidad):
        self.capacidad=capacidad
        self.tipo="SSD"

class Teclado():
    def __init__(self, idioma: str, cantidad_teclas: int):
        self.idioma = idioma
        self.cantidad_teclas = cantidad_teclas
        
class Mouse():
    def __init__(self, tipo:str, conectividad: str):
        self.tipo = tipo
        self.conectividad = conectividad

class Computador():
    def __init__(self, teclado : Teclado, mouse: Mouse):
        #computador está compuesto de...
        self.ram=Ram(4000)  #composición, a un atributo asignarle una clase de forma INTERNA
        self.disco_duro=DiscoDuro(1024)
        
        self.teclado= teclado
        self.mouse=mouse

#instancias de clase    
teclado = Teclado("esp", 120)
mouse = Mouse("Gamer", "Bluetooth")

computador_gamer = Computador(teclado, mouse) #AGREGACIÓN
print(computador_gamer.ram.velocidad) #4000
print(computador_gamer.teclado.cantidad_teclas) #120
