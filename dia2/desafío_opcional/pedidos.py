from te import Te



sabor = int(input("""Ingrese el tipo de te que desea pedir: [1, 2 o 3]
                1) Té Negro
                2) Té Verde
                3) Agua de hierbas
                """))
gramaje = int(input("""¿Cuántos gramos desea pedir?: [1 o 2]
                    1) 300 gramos
                    2) 500 gramos
                    """))
print("------------------------------------")
Te.especificaciones(sabor)
print(f"El precio para esta cantidad de gramos es de {Te.precio_gramaje(gramaje)} pesos chilenos")