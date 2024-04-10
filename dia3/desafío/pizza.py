from ingredientes import lista_masa,lista_proteinas,lista_vegetales
class Pizza():
    tamaño = "familiar"
    precio = 10000
    tipo_masa = ""
    ingredientes = []

    @staticmethod
    def validar(ingrediente: str, lista: list):
        return ingrediente in lista  #mejora al revisar
        
    
    def tomar_pedido(self): #versión más breve del método, validar al final
        self.proteina = input("Ingrese su ingrediente proteico [carne, pollo o soya]: ").lower()
        self.ingredientes.append(self.proteina)
        self.vegetal_1 = input("Ingrese su primer ingrediente vegetal [tomate, aceituna o champiñones]: ").lower()
        self.ingredientes.append(self.vegetal_1)

        self.vegetal_2 = input("Ingrese su segundo ingrediente vegetal [tomate, aceituna o champiñones]: ").lower()
        self.ingredientes.append(self.vegetal_2)
        self.masa = input("Seleccione el tipo de masa [tradicional o delgada]: ").lower()
        self.tipo_masa = self.masa
        
        self.es_pizza_valida = self.validar(self.proteina,lista_proteinas) and \
        self.validar(self.vegetal_1,lista_vegetales) and \
        self.validar(self.vegetal_2, lista_vegetales) and \
        self.validar(self.masa, lista_masa)   #mejora en revisión :validar en un nuevo atributo
            

if __name__ == "__main__":
    print(Pizza.validar("tomate", lista_vegetales))
    print(Pizza.validar("pollo", lista_proteinas))
    print(Pizza.validar("tradicional", lista_masa))
    print(Pizza.validar("cebolla", lista_vegetales))
    print(Pizza.validar("caballo", lista_proteinas))
    print(Pizza.validar("de sopaipilla", lista_masa))
    pedido = Pizza()
    pedido.tomar_pedido()
    
    
            
                
            
            
    