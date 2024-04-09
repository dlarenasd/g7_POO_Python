from pelota import Pelota

#creación de objeto o instancia de la clase
pelota_multicolor = Pelota()
#print(pelota_multicolor.color) #AttributeError: 'Pelota' object has no attribute 'color'
pelota_multicolor.asigna_color("rojo")
print(pelota_multicolor.color) #rojo -> ahora si existe ese atributo
pelota_multicolor.lee_color() #El color de esta pelota es rojo
#
pelota_multicolor.asigna_color("verde")
pelota_multicolor.lee_color_local_y_atributo("amarillo")

pelota_negra = Pelota()
pelota_negra.lee_color_local_y_atributo("negro")