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

