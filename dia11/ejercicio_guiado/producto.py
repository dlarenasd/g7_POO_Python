import json

instancias = [] #lista vacía para almacenar

with open ("productos.txt") as productos: #abrir un archivo y darle un alias
    linea = productos.readline() #la variable linea contendrá lo que encuentres en una linea de productos
    while linea: #mientras tenga contenido la variable...
        producto = json.loads(linea) #un producto será esa línea pero dándole formato con json.loads (vienen en json)


class Producto(): #clase para instanciar productos
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio
        
instancias.append(Producto(producto.get("nombre"), producto.get("precio"))) #generar y almacenar una instancia de Producto a partir de los datos
#de producto (lineas json)

#el ultimo paso es actualizar la variable linea, así vamos generando productos a partir de las demas lineas del txt