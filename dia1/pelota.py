class Pelota():
    forma = "redondeada" # atributo de clase
    material = ""
    posiciones = [3,0,2,1,0]
    
    #Método estático
    @staticmethod #decorador para especificar que es un método estático
    def crear_rebote():
        return[5,0,4,0,3,0,2,0,1,0]
    
    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote() #llamar a un método estático
        print(Pelota.posiciones) #imprimir un atributo de clase
    
    #método no estático o de instancia, SIEMPRE van con self como parámetro
    #modificación del estado de un objeto
    def rebotar(self):
        self.posiciones = self.crear_rebote()
        
    def nuevo_atributo(self):
        self.color = "blanco" #en el método creamos un atributo que no existe