class Pelota():
    #atributos de clase
    marca = "adidas"
    #Método Constructor
    def __init__(self, color:str, tamaño=20, material="plástico"): #es un método no estático// se pueden asignar los tipos de valores para los atributos,
        #igualmente se pueden establecer valores por defecto para los atributos de instancia  
        print("Método constructor al crear la instancia de clase")
        self.__color = color
        self.tamaño = tamaño
        self.material = material
        self.rebote = 0 #este atributo no lo incluyo para ser ingresado por argumento, pero lo dejo creado para definirlo después por método o desde la instancia
        self.marca = "Adidas"
        self.__password = "qwerty"
    
    #método oculto    
    def __getColor(self):
        return self.__color
    
    def setColor(self,color): #-->asignar color como método
        self.__color = color
        
    def setPassword(self,password):
        self.__password = password
        
    #método getter --> permite acceder a los atributos ocultos
    @property 
    def color(self):
        return self.__color
    #método setter --> permite acceder y modificar atributos ocultos, teniendo un getter hecho previamente
    @color.setter  #TIENE QUE TENER EL MISMO NOMBRE
    def color(self,color: str): 
        self.__color = color if color != "" else "Verde"
    
    #método deleter
    @color.deleter
    def color(self):
        del self.__color


    
pelota_de_futbol = Pelota("amarillo", 16, "plástico")#de esta forma se ingresan los valores que ocuparán los atributos
#print(pelota_de_futbol.color) #AttributeError: 'Pelota' object has no attribute 'color'--->al incluir los dos guiones bajos al atributo se oculta el atributo, deja de ser accesible/visible
#print("getColor()", pelota_de_futbol.getColor()) # mediante un método específico para acceder al atributo se puede, a menos que con __ lo oculten también
print("método getter", pelota_de_futbol.color) #color SIN PARÉNTESIS, no es un método, es una propiedad de la clase definido en la línea 19-21
print(pelota_de_futbol.tamaño)
#pelota1=Pelota() TypeError: Pelota.__init__() missing 3 required positional arguments: 'color', 'tamaño', and 'material' --> ya no acepta el uso de clase sin argumentos
pelota3 = Pelota("Rojo")
#print(pelota3.color,pelota3.tamaño, pelota3.material) #Rojo 20 plástico
