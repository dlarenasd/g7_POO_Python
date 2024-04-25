from abc import ABC, abstractmethod
from error import SubTipoInvalidoError
#se importan las clases necesarias para hacer una clase abstracta y gatillar un error específico del programa
class Anuncio(ABC): #clase abstracta de Anuncios
    SUB_TIPOS = None #atributos de clase que va a heredar
    __sub_tipo = None
    FORMATOS = ("Video", "Display", "Social") #formatos de anuncio disponibles
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str): #constructor
        if ancho <= 0: #validar que si ancho y/o alto son menores a uno pasen a valer uno, en el caso contrario toman el valor ingresado por parámtro
            self.__ancho = 1
        else:
            self.__ancho = ancho
        if alto <= 0:
            self.__alto = 1
        else:
            self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic

    @staticmethod
    def mostrar_formatos(): #método estático que usa colaboración
        v = Video("", "", 1,) #instancias de prueba para el método
        d = Display(1,1,"","")
        s = Social(1,1,"","")
        print(f"""
Formato 1: {Anuncio.FORMATOS[0]}\n===============\nSubtipos:\n- {Video.SUB_TIPOS[0]}\n- {Video.SUB_TIPOS[1]} \n
Formato 2: {Anuncio.FORMATOS[1]}\n===============\nSubtipos:\n- {Display.SUB_TIPOS[0]}\n- {Display.SUB_TIPOS[1]} \n
Formato 3: {Anuncio.FORMATOS[2]}\n===============\nSubtipos:\n- {Social.SUB_TIPOS[0]}\n- {Social.SUB_TIPOS[1]}
""") #método retorna cada uno de los formatos con sus sub-tipos usando colaboración
    
    @abstractmethod
    def comprimir_anuncio(self): #métodos abstractos que deben ser implementados en las sub-clases
        pass
    @abstractmethod
    def redimensionar_anuncio(self):
        pass
    
    @property
    def sub_tipo(self): #getter
        return self.__sub_tipo
    @sub_tipo.setter #setter
    def sub_tipo(self, tipo):
        if tipo in self.SUB_TIPOS: #validación al modificar el sub-tipo, si está dentro de la tupla lo asigna
            self.__sub_tipo = tipo
            return self.__sub_tipo
        else: #en el caso contrario gatilla un error específico
            raise SubTipoInvalidoError("Error: Subtipo no válido", self.SUB_TIPOS) #al lanzar el error se incluye un mensaje y la tupla de opciones


    @property
    def url_archivo(self): #getter
        return self.__url_archivo
    @url_archivo.setter #setter
    def url_archivo(self, url_archivo:str):
        self.__url_archivo = url_archivo
        return self.__url_archivo
    
    @property
    def url_clic(self): #getter 
        return self.__url_clic
    @url_clic.setter #setter
    def url_clic(self, url_clic:str):
        self.__url_clic = url_clic
        return self.__url_clic

class Video(Anuncio): #clase video, hija de anuncio
    SUB_TIPOS = ("instream", "outstream") #tiene una tupla con dos sub_tipos disponibles
    def __init__(self, url_archivo: str, url_clic: str, duracion:int, ancho = 1, alto = 1): #constructor heredado y modificado
        if ancho != 1: #validar valores de ancho y alto y asignar valores por defecto
            ancho = 1
        if alto != 1:
            alto = 1
        super().__init__(ancho, alto, url_archivo, url_clic)
        if duracion <= 0: #incluir validación a parámetro nuevo
            self.__duracion = 5
        else: 
            self.__duracion = duracion
        
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN") #métodos abstractos sin implementar
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
    
    @property
    def duracion(self): #getter
        return self.__duracion
    @duracion.setter  #setter
    def duracion(self, duracion):
        if duracion <= 0:
            self.__duracion = 5
        else: 
            self.__duracion = duracion
    
class Display(Anuncio): #igual que video, pero con otra tupla
    SUB_TIPOS = ("tradicional", "native")
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):#igual que video, pero con otra tupla
    SUB_TIPOS = ("facebook", "linkedin")
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
    
if __name__ == "__main__":
    anuncio = Video("", "", -60, -5,-5 )
    anuncio.mostrar_formatos()
    print(anuncio.duracion)
    anuncio.comprimir_anuncio()
    anuncio.redimensionar_anuncio()
    print(anuncio.FORMATOS)
    print(anuncio.SUB_TIPOS)
    print(anuncio.sub_tipo)
    anuncio.sub_tipo = "outstream"
    print(anuncio.sub_tipo)