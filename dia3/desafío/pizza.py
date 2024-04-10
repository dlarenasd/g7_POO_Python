from ingredientes import lista_masa,lista_proteinas,lista_vegetales
class Pizza():
    tamaño = "familiar"
    precio = 10000
    tipo_masa = ""
    ingredientes = []

    @staticmethod
    def validar(ingrediente: str, lista: list):
        return ingrediente in lista  #mejora al revisar
        
    
    def tomar_pedido(self):
        while len(self.ingredientes) <1:
            proteina = input("Ingrese su ingrediente proteico [carne, pollo o soya]: ").lower()
            es_valido = self.validar(proteina,self.lista_proteinas)
            if es_valido == True:
                print("Ingrediente válido, continuemos con los vegetales")
                self.ingredientes.append(proteina)
            else:
                print("Ingrediente no válido")
        while len(self.ingredientes) == 1:
            vegetal_1 = input("Ingrese su primer ingrediente vegetal [tomate, aceituna o champiñones]: ").lower()
            validar = self.validar(vegetal_1,self.lista_vegetales)
            if validar == True:
                print("Ingrediente válido")
                self.ingredientes.append(vegetal_1)
            else:
                print("Ingrediente no válido")
        while len(self.ingredientes) == 2:
            vegetal_2 = input("Ingrese su segundo ingrediente vegetal [tomate, aceituna o champiñones]: ").lower()
            validar = self.validar(vegetal_2,self.lista_vegetales)
            if validar == True:
                print("Ingrediente válido")
                self.ingredientes.append(vegetal_2)
            else:
                print("Ingrediente no válido")
        while len(self.ingredientes) ==3:
            masa = input("Seleccione el tipo de masa [tradicional o delgada]: ").lower()
            validar = self.validar(masa,self.lista_masa)
            if validar == True:
                self.tipo_masa = masa
                print("Masa válida, tu pedido ya está armado")
                break
        if self.validar(proteina,self.lista_proteinas) and self.validar(vegetal_1,self.lista_vegetales) and self.validar(vegetal_2, self.lista_vegetales) and self.validar(masa, self.lista_masa) == True:
            print(f"Tus ingredientes son {self.ingredientes} y tu masa es {self.tipo_masa}.")
            valid = True
        else: 
            valid = False
        return valid

            

if __name__ == "__main__":
    print(Pizza.validar("tomate", lista_vegetales))
    print(Pizza.validar("pollo", lista_proteinas))
    print(Pizza.validar("tradicional", lista_masa))
    print(Pizza.validar("cebolla", lista_vegetales))
    print(Pizza.validar("caballo", lista_proteinas))
    print(Pizza.validar("de sopaipilla", lista_masa))
    pedido = Pizza()
    pedido.tomar_pedido()
    
    
            
                
            
            
    