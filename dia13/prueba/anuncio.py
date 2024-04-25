from abc import ABC, abstractmethod
from error import SubTipoInvalidoError
#se importan las clases necesarias para hacer una clase abstracta y gatillar un error específico del programa

class Anuncio(ABC): #clase abstracta de Anuncios
    
    FORMATOS = ("Video", "Display", "Social") #formatos de anuncio disponibles
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str): #constructor
        self.__ancho = ancho if ancho >0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos(): #método estático que usa colaboración
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
        # try: SI AQUÍ USO TRY/EXCEPT NO PUEDO USARLO EN EL OTRO SCRIPT, POR LO QUE NO GENERA UN ERROR.LOG
            if tipo not in self.SUB_TIPOS: #validación al modificar el sub-tipo, si está dentro de la tupla lo asigna
                raise SubTipoInvalidoError #se lanza el error
            else: 
                self.__sub_tipo = tipo
        # except SubTipoInvalidoError as error:
        #   print(error)
            
    @property
    def ancho(self): #getter
        return self.__ancho
    @ancho.setter #setter
    def ancho(self, ancho:int):
        self.__ancho = ancho if ancho > 0 else 1
        return self.__ancho
    
    @property
    def alto(self): #getter
        return self.__alto
    @alto.setter #setter
    def alto(self, alto:int):
        self.__ancho = alto if alto >0 else 1
        return self.__alto
    
    @property
    def url_archivo(self): #getter
        return self.__url_archivo
    @url_archivo.setter #setter
    def url_archivo(self, url_archivo:str):
        self.__url_archivo = url_archivo
        return self.__url_archivo

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
    
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion:int): #constructor heredado y modificado
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5
        
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN") #métodos abstractos sin implementar
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
    
    @property
    def duracion(self): #getter
        return self.__duracion
    @duracion.setter  #setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5
    @property #modificar el setter, para que no puedan modificar ancho
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self):
        pass
    
    @property #modificar el setter, para que no puedan modificar alto
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self):
        pass
    
    
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
    
if __name__ == "__main__":  #pruebas del script, métodos de clase e instancia
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