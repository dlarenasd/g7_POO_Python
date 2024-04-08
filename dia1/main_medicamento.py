from medicamento import Medicamento

#instancia de la clase o creación de un objeto UN OBJETO PERTENECE A SOLO UNA CLASE
paracetamol = Medicamento()

aspirina = Medicamento() #otro objeto de la misma clase

print(paracetamol.descuento) #0.05
print(aspirina.descuento) #0.05

paracetamol.descuento = 0.06
print(paracetamol.descuento) #0.06 modificamos el valor del atributo de forma individual al objeto, sin afectar el atributo para los demás objetos de la clase