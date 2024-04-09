from medicamento import Medicamento

#paso 1: crear instancia
medicamento_nuevo = Medicamento()

#solicitud de ingreso de datos
precio = int(input("Ingrese el precio del medicamento: "))

#pasar al método de instancia el valor capturado
medicamento_nuevo.asigna_precio(precio)
print(f"El precio es: ${medicamento_nuevo.precio}")
print(f"El descuento es: {medicamento_nuevo.descuento*100}%")
print(f"El precio final es: {medicamento_nuevo.precio-(medicamento_nuevo.precio * medicamento_nuevo.descuento)}")

#NO SE PUEDE LLAMAR A UN MÉTODO NO ESTÁTICO DESDE UNA CLASE, SOLO DESDE UN OBJETO