import json
from datetime import datetime

now=datetime.now()

class Producto(): #clase para instanciar productos
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio
        
instancias = [] #lista vacía para almacenar
with open ("dia13/ejercicio/manejo_archivos/productos.txt") as productos: #abrir un archivo y darle un alias
    for linea in productos.readlines(): #la variable linea contendrá lo que encuentres en una linea de productos
        try:
            producto = json.loads(linea) #un producto será esa línea pero dándole formato con json.loads (vienen en json)
            instancias.append(Producto(producto.get("nombre"), producto.get("precio"))) #generar y almacenar una instancia de Producto a partir de los datos
            #de producto (lineas json)
        except Exception as error:
            with open ("dia13/ejercicio/manejo_archivos/error.log", "a+", encoding="utf-8") as errorlog:
                errorlog.write(f"[{now.strftime("%Y/%m/%d, %H:%M:%S")}] Error: Algo hizo mal.\n")
                errorlog.close()
productos.close()


#el ultimo paso es actualizar la variable linea, así vamos generando productos a partir de las demas lineas del txt
print(f"{instancias}")