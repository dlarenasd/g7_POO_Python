class Te():
    formato =[300,500]
    duración = "1 año"
    infusión = ""
    recomendación = ""
    
    @staticmethod
    def especificaciones(num:int):
        if num == 1:
            print("Las especificaciones para el té negro son las siguientes: ")
            print(f"El tiempo de infusión es de {Te.infusión}.")
            print(f"Se recomienda {Te.recomendación}.")
            print(f"Recuerde consumir antes de {Te.duración}.")
        elif num == 2:
            print("Las especificaciones para el té verde son las siguientes: ")
            print(f"El tiempo de infusión es de {Te.infusión}.")
            print(f"Se recomienda {Te.recomendación}.")
            print(f"Recuerde consumir antes de {Te.duración}.")
        elif num == 3:
            print("Las especificaciones para el agua de hierbas son las siguientes: ")
            print(f"El tiempo de infusión es de {Te.infusión}")
            print(f"Se recomienda {Te.recomendación}.")
            print(f"Recuerde consumir antes de {Te.duración}.")
    
    @staticmethod
    def precio_gramaje(num:int):
        if num == 1:
            precio = 3000
        elif num == 2:
            precio = 5000
        return precio

    def asignar_infusion(self, nuevo_valor):
        self.infusión = nuevo_valor
    def asignar_recomendación(self, nueva_recomendacion):
        self.recomendación = nueva_recomendacion


if __name__ == "__main__":
    Te.especificaciones(2)
    print(Te.precio_gramaje(1))
