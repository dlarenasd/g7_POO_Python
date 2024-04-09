class Te():
    formato =[300,500]
    duración = "1 año"
    infusión = ""
    recomendación = ""
    
    @staticmethod
    def especificaciones(num:int):
        if num == 1:
            print("Las especificaciones para el té negro son las siguientes: ")
            Te.infusión = "3 minutos"
            print(f"El tiempo de infusión es de {Te.infusión}.")
            Te.recomendación = "consumir en el desayuno"
            print(f"Se recomienda {Te.recomendación}.")
            print(f"Recuerde consumir antes de {Te.duración}.")
        elif num == 2:
            print("Las especificaciones para el té verde son las siguientes: ")
            Te.infusión = "5 minutos"
            print(f"El tiempo de infusión es de {Te.infusión}.")
            Te.recomendación = "consumir al mediodía"
            print(f"Se recomienda {Te.recomendación}.")
            print(f"Recuerde consumir antes de {Te.duración}.")
        elif num == 3:
            print("Las especificaciones para el agua de hierbas son las siguientes: ")
            Te.infusión = "6 minutos"
            print(f"El tiempo de infusión es de {Te.infusión}.")
            Te.recomendación = "consumir al atardecer"
            print(f"Se recomienda {Te.recomendación}.")
            print(f"Recuerde consumir antes de {Te.duración}.")
            
    @staticmethod
    def precio_gramaje(num:int):
        if num == 1:
            precio = 3000
        elif num == 2:
            precio = 5000
        return precio
    

if __name__ == "__main__":
    Te.especificaciones(2)
    print(Te.precio_gramaje(1))
