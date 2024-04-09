from dia2.probando_cosas import Te

te_negro = Te()
te_verde = Te()
agua_de_hierbas = Te()

te_negro.asignar_infusion("3 minutos")
te_verde.asignar_infusion("5 minutos")
agua_de_hierbas.asignar_infusion("6 minutos")

te_negro.asignar_recomendación("consumir en el desayuno")
te_verde.asignar_recomendación("consumir al mediodía")
agua_de_hierbas.asignar_recomendación("consumir al atardecer")

sabor = int(input("""Ingrese el tipo de te que desea pedir: [1, 2 o 3]
                1) Té Negro
                2) Té Verde
                3) Agua de hierbas
                """))
gramaje = int(input("""¿Cuántos gramos desea pedir?: [1 o 2]
                    1) 300 gramos
                    2) 500 gramos
                    """))

print(Te.especificaciones(sabor))
print(f"El precio para esta cantidad de gramos es de {Te.precio_gramaje(gramaje)} pesos chilenos")