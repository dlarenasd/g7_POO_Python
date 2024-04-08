from medicamento import Medicamento

#instancia de la clase o creación de un objeto UN OBJETO PERTENECE A SOLO UNA CLASE
paracetamol = Medicamento()

aspirina = Medicamento() #otro objeto de la misma clase

print(paracetamol.descuento) #0.05
print(aspirina.descuento) #0.05

paracetamol.descuento = 0.06 #modificación del estado de un objeto --> modificación del valor de un atributo DENTRO de un objeto
print(paracetamol.descuento) #0.06 modificamos el valor del atributo de forma individual al objeto, sin afectar el atributo para los demás objetos de la clase
print(aspirina.descuento)

Medicamento.descuento = 0.04 #modificación exclusiva para este módulo y para todas las líneas a continuación, no impacta otros script
ibuprofeno = Medicamento()
print(ibuprofeno.descuento) #0.04   

precio = int(input("Ingrese el precio a validar -> "))
#llamado a un método estático
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es válido")
else:
    print("El precio ingresado NO es válido")

print(paracetamol.descuento)
print(aspirina.descuento)

if paracetamol.IVA == aspirina.IVA and paracetamol.descuento == aspirina.descuento:
    print("Todas las instancias (objetos) tienen los mismos valores de IVA y descuento")
    print(f"IVA: {Medicamento.IVA}")
    print(f"Descuento: {Medicamento.descuento}") #---> al imprimir esto, dado que hicimos una modificación del atributo descuento
    #ahora sale su valor modificado, no el de los objetos

ibuprofeno.modificar_atributo() #el objeto llama al método y cambia su atributo, pero al hacerlo cambia el atributo de la clase, para todos los objetos
print(ibuprofeno.IVA , aspirina.IVA) 
print(ibuprofeno.descuento, aspirina.descuento, paracetamol.descuento) #paracetamol tuvo una modificación particular, 
#ese valor pesa más que la modificación para la clase completa