from pizza import Pizza

#script hecho en revisión

"""a. Usar la función print(), para que al ejecutar el script se muestre en pantalla los
valores de los atributos de clase de la clase importada, sin crear una instancia
de ella."""
print(f"El tamaño de la pizza es {Pizza.tamaño}, su valor es ${Pizza.precio} pesos chilenos")


"""b. Usar la función print(), para que al ejecutar el script se muestre en pantalla
si el elemento “salsa de tomate” se encuentra presente en la lista [“salsa de
tomate", "salsa bbq"]. Para ello use el método creado en el requerimiento
2, sin crear una instancia de la clase importada."""

print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa bbq"]))


"""c. Crear una instancia de la clase importada, y luego llamar al método del
requerimiento 3, para que al ejecutar el script se solicite ingredientes y tipo de
masa al usuario."""

pedido = Pizza()
pedido.tomar_pedido()

"""d. Usar la función print(), para que al ejecutar el script, luego de que el usuario
haya ingresado los ingredientes y tipo de masa, se muestre en pantalla los
ingredientes vegetales, el ingrediente proteico y el tipo de masa de la instancia
creada en el paso anterior, y si esa instancia es una pizza válida o no."""

if pedido.es_pizza_valida:
    print("Su pizza es válida")
    print(f"Los ingredientes son: {pedido.ingredientes[0]}, {pedido.ingredientes[1]} y {pedido.ingredientes[2]}.")
    print(f"El tipo de masa es: {pedido.tipo_masa}.")
else:
    print("La pizza no es válida")



"""e. Usar la función print(), para mostrar en pantalla si la clase Pizza es una pizza
válida o no, haciendo uso del atributo creado en el requerimiento 4, sin crear
una instancia de la clase. En este punto, la ejecución del script debe mostrar
un error (todos los pasos anteriores se deben haber ejecutado correctamente)."""

print(Pizza.es_pizza_valida)