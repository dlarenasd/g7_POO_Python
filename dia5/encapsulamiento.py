class Auto:
    __color = "Blanco"
    
    def __cambia_color(self,color):
        print("Nuevo color",color)
        self.__color = color
    def imprimir_estado(self,nuevo_color):
        print(self.__color)
        self.__cambia_color(nuevo_color)
        print(self.color)
    
    #getter --> Obtener un valor    
    @property
    def color(self):
        return self.__color
nissan = Auto()
#print(nissan.__color)
#print(Auto.__color)

#nissan.cambia_color("Rojo") 
nissan.imprimir_estado("Negro")
print("")
print(nissan.color) #llamado al método getter
print(nissan._Auto__color)