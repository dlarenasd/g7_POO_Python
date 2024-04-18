"""
Diego Larenas
Claudio Méndez
Juan Torres 

"""


from abc import ABC, abstractmethod
from producto import Producto
class Tienda(ABC):
    #CLASE ABSTRACTA PARA GENERAR TIENDAS
    nombre_tienda = "" #incluye los atributos de la clase que va a heredar
    costo_delivery= ""
    @abstractmethod
    def ingresar_producto(self): #incluye los 3 métodos abstractos que se solicitan
        pass
    @abstractmethod
    def listar_productos(self):
        pass
    @abstractmethod
    def venta_producto(self):
        pass
    
    
class Restaurant(Tienda):
    def __init__(self, nombre_tienda:str, costo_delivery:int): #constructor de la clase, entran por parámetro los valores de los atributos
        self.__nombre_tienda = nombre_tienda #los atributos de instancia son privados
        self.__costo_delivery = costo_delivery
        self.lista_productos = [] #lista vacía que va a recibir los objetos de clase productos
    
    @property
    def nombre_tienda(self): #getter de atributo privado
        return self.__nombre_tienda
    @property
    def costo_delivery(self): #getter de atributo privado // NO SE INCLUYE SETTER PORQUE NO SON MODIFICABLES
        return self.__costo_delivery
    
    def ingresar_producto(self, nombre_producto: str, precio_producto: int): #dado que los productos de Restaurant siempre tienen stock 0
        producto = Producto(nombre_producto, precio_producto) # no se incluye el parámetro de stock
        if producto in self.lista_productos: #identificar si el producto ingresado ya está en la lista mediante sobrecarga de __eq__
            return "Producto ingresado" #mensaje para confirmar el ingreso, pero sin modificar ningún atributo
        else:
            self.lista_productos.append(producto) #si no está, se incluye el producto a la lista (con su atributo nombre y atributo precio)
            return "Producto ingresado"
    
    def listar_productos(self): #Método para poder mostrar la lista de productos
        retorno = (""":::::::::::LISTA DE PRODUCTOS:::::::::::\n
Nombre: \t Precio: \t Stock:\n """) #variable con texto base
        lista_string = [f"{producto}" for producto in self.lista_productos] #traspaso de los elementos de la lista productos a un string ordenado
        return f"{retorno}{"".join(lista_string)}"  #retorna el mensaje base, debajo de él entrega la concatenación 
                                                            #de los elementos de la lista recién hecha 
                                                            #se explicita que el retorno debe ser un string en la pauta

    def venta_producto(self, nombre_producto:str, cantidad:int):
        pass #los restaurant no necesitan el método venta_producto ya que su stock siempre es 0     
    

class Supermercado(Tienda): #Mismo esqueleto del restaurant
    def __init__(self, nombre_tienda:str, costo_delivery:int):
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.lista_productos = []
    
    @property
    def nombre_tienda(self):
        return self.__nombre_tienda
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    def ingresar_producto(self, nombre_producto: str, precio_producto: int, stock_producto: int):
        producto = Producto(nombre_producto, precio_producto, stock_producto) #en el supermercado si hay ingreso de stock
        if producto in self.lista_productos: #la validación es diferente, si el producto está en la lista se va a ubicar su índice
            indice = self.lista_productos.index(producto)
            self.lista_productos[indice]+= producto  #y luego de ubicar el índice se va a sumar el stock adicional al producto
            return "Stock actualizado"  #Mensaje de confirmación // Se usó la sobrecarga de __eq__ y sobrecarga de __iadd__ para sumar 
        else:                                                       #el stock de objetos con el mismo nombre
            self.lista_productos.append(producto) #si no está en la lista se incluye
            return "Producto ingresado" # mensaje de confirmación
    
    def listar_productos(self): #mismo método de antes
        retorno = (""":::::::::::LISTA DE PRODUCTOS:::::::::::\n
Nombre: \t Precio: \t Stock:\n """)
        lista_string = [f"{producto}" for producto in self.lista_productos]
        return f"{retorno}{"".join(lista_string)}" 

    def venta_producto(self, nombre_producto:str, cantidad:int): #método de venta, se ingresa un nombre de producto y una cantidad
        objeto = Producto(nombre_producto, 0, cantidad) #se elabora un objeto como producto para comparar a continuación
        if objeto in self.lista_productos: #compara y busca un objeto con el mimso nombre en la lista
            indice = self.lista_productos.index(objeto) #ubica su índice
            if self.lista_productos[indice].stock_producto == 0: #si el stock es 0 lo notifica
                return "Producto sin stock"
            elif self.lista_productos[indice].stock_producto >= cantidad: #si hay mas stock que lo que piden 
                self.lista_productos[indice].stock_producto -= cantidad #resta la cantidad al stock del producto
                return f"Se vendieron {cantidad} {self.lista_productos[indice].nombre_producto}"    #se retorna un mensaje
            else:
                print(f"Se vendieron {self.lista_productos[indice].stock_producto} {self.lista_productos[indice].nombre_producto}")
                self.lista_productos[indice].stock_producto -= self.lista_productos[indice].stock_producto #si hay menos stock que cantidad
                return "Se vendieron todos los productos disponibles" #se resta el stock consigo mismo, deja el stock en 0 y notifica cuánto vendió
        else:
            return "No se encuentra el producto solicitado" #si no hay coincidencia lo notifica

        
class Farmacia(Tienda):
    def __init__(self, nombre_tienda:str, costo_delivery:int):
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.lista_productos = []
    
    @property
    def nombre_tienda(self):
        return self.__nombre_tienda
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    def ingresar_producto(self, nombre_producto: str, precio_producto: int, stock_producto: int):
        producto = Producto(nombre_producto, precio_producto, stock_producto)
        if producto in self.lista_productos:
            indice = self.lista_productos.index(producto)
            self.lista_productos[indice]+= producto
            return "Stock actualizado"
        else:
            self.lista_productos.append(producto)
            return "Producto ingresado"
    
    def listar_productos(self):
        retorno = (""":::::::::::LISTA DE PRODUCTOS:::::::::::\n
Nombre: \t Precio: \t Stock:\n """)        
        lista_string = [f"{producto}" for producto in self.lista_productos]
        return f"{retorno}{"".join(lista_string)}" 

    def venta_producto(self, nombre_producto:str, cantidad:int):
        objeto = Producto(nombre_producto, 0, cantidad)
        if cantidad > 3: #única diferencia: si pides mas de 3 unidades en la farmacia el programa rechaza la venta
            return "Venta rechazada, no se puede vender más de 3 unidades"
        elif objeto in self.lista_productos:
            indice = self.lista_productos.index(objeto)
            if self.lista_productos[indice].stock_producto == 0:
                return "Producto sin stock"
            elif self.lista_productos[indice].stock_producto >= cantidad:
                self.lista_productos[indice].stock_producto -= cantidad
                return f"Se vendieron {cantidad} {self.lista_productos[indice].nombre_producto}"    
            else:
                print(f"Se vendieron {self.lista_productos[indice].stock_producto} {self.lista_productos[indice].nombre_producto}")
                self.lista_productos[indice].stock_producto -= self.lista_productos[indice].stock_producto
                return "Se vendieron todos los productos disponibles"
        else:
            return "No se encuentra el producto solicitado"



if __name__ == "__main__":
    domino = Restaurant("dominó",1500) #creación de un objeto de clase Restaurant para validar (nombre_local, cost_delivery)
    print(domino.ingresar_producto("completo", 1200)) #validar ingreso en restaurant
    print(domino.ingresar_producto("completo", 1500)) #validar que no sobreescriba el precio si ya está ingresado
    print(domino.ingresar_producto("dinámico", 1200)) #más productos
    print(domino.ingresar_producto("italiano", 1500)) #más productos
    print(domino.lista_productos[1]) #imprimir cómo se muestra un solo objeto de la lista
    print(domino.listar_productos()) #validar funcionamiento de listar_productos
    print("")
    unimarc = Supermercado("Unimarc", 1000) #creación de un objeto de clase Supermercado para validar (nombre_local, cost_delivery)
    print(unimarc.ingresar_producto("arroz", 800, 30 ))
    print(unimarc.ingresar_producto("arroz", 200, 20 ))
    print(unimarc.ingresar_producto("atún", 750, 25 ))
    print(unimarc.ingresar_producto("café", 1000, 8 ))
    print("")
    print(unimarc.listar_productos())
    print(unimarc.venta_producto("atún", 26))
    print(unimarc.listar_productos())
    print("")
    simi = Farmacia("Dr.Simi", 0)
    print(simi.ingresar_producto("paracetamol", 800, 30 ))
    print(simi.ingresar_producto("paracetamol", 200, 20 ))
    print(simi.ingresar_producto("ibuprofeno", 750, 25 ))
    print(simi.ingresar_producto("sertralina", 1000, 8 ))
    print("")
    print(simi.listar_productos())
    print(simi.venta_producto("sertralina", 5))
    print(simi.venta_producto("sertralina", 3))
    print(simi.venta_producto("sertralina", 3))
    print(simi.listar_productos())
    print(simi.venta_producto("sertralina", 3))
    print(simi.venta_producto("sertralina", 3))
    print(simi.listar_productos())
    

    
