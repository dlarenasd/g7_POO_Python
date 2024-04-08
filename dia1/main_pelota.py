#import pelota
from pelota import Pelota
"""
instanciar o crear un objeto

definir una variable y asignarle la clase (a partir del módulo importado)
"""
#pelota_de_andy = pelota.Pelota()
pelota_de_andy = Pelota()

print(pelota_de_andy) #<pelota.Pelota object at 0x00000265954A9820>
print(type(pelota_de_andy)) # <class 'pelota.Pelota'>
print(pelota_de_andy.forma) #redondeada -->hereda los atributos de su clase por default
print(pelota_de_andy.material) # si aún no asigno un valor al atributo imprime vacío

pelota_de_andy.material = "Plástico" # material es un atributo de clase, con un valor para instancia exclusivo de la pelota de andy
print(pelota_de_andy.material) #ahora que se le asignó un valor tiene un atributo

pelota_de_tenis = Pelota()
print(pelota_de_tenis.material) #el nuevo objeto tiene el atributo material, pero no tiene el valor plástico que le asginamos a pelota de andy
pelota_de_tenis.material = "Caucho"
print(pelota_de_tenis.material) #al objeto le daremos el valor para instancia a su atributo de clase que no estaba definido
print(pelota_de_tenis.posiciones) # [3, 0, 2, 1, 0] al ser creada previo a la modificación del atributo, no cambia el valor del atributo

#Métodos estáticos no requieren de una instancia para llamar al método
print(Pelota.crear_rebote) #<function Pelota.crear_rebote at 0x000001DAA3B9DBC0>
print(Pelota.crear_rebote()) #[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

Pelota.imprimir_posiciones() #[3, 0, 2, 1, 0] meimprime la lista posiciones que es un atributo de la clase Pelota, en el método solicito la impresión
print(Pelota.posiciones) #[3, 0, 2, 1, 0]
Pelota.posiciones = [2,4,6] #asignarle un nuevo valor al atributo
Pelota.imprimir_posiciones() #[2, 4, 6]se modificó el valor del atributo por medio de la clase
print(Pelota.posiciones) #[2, 4, 6] 
print("")
pelota_de_futbol = Pelota()
print(pelota_de_futbol.posiciones) #[2, 4, 6] #al ser creada luego de la modificación tiene el nuevo valor sociado a su atributo

#MÉTODOS NO ESTÁTICOS
pelota_de_futbol.rebotar() #modificamos el valor de un atributo mediante un método de la clase, no con un cambio en el script
print(pelota_de_futbol.posiciones) #[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

pelota_de_basket = Pelota()
print(pelota_de_basket.posiciones) #[2, 4, 6] --> tiene la modificación del script (línea 31), no como la pelota de fútbol a la que se le hizo una modificación con un método de clase
#Los métodos no estáticos, permiten crear atributos de tipo "atributo de instancia"
pelota_de_basket.nuevo_atributo()
print(pelota_de_basket.color) #blanco
print(pelota_de_andy.color) #AttributeError: 'Pelota' object has no attribute 'color'