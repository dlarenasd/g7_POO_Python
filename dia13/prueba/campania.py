from anuncio import Video,Display,Social
from error import LargoExcedidoError


class Campaña(): #clase que instacia objetos campaña
    def __init__(self, nombre: str, fecha_inicio:str, fecha_termino:str, anuncios:list): #en su constructor se agrega una lista de anuncios, aparte de nombre y fechas
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [] #lista vacía que va a almacenar los objetos de clase video, display y/o social
        for anuncio in anuncios: #recorro la lista ingresada por parámetro
            if anuncio["formato"]=="Video": #busca la clave formato, si su formato es video, instancia un video
                self.__anuncios.append(Video(anuncio["url_archivo"],anuncio["url_clic"], anuncio["duracion"])) #saca los parámetros que necesita del diccionario
            elif anuncio["formato"]=="Display": #mismo procedimiento con display
                self.__anuncios.append(Display(anuncio["ancho"], anuncio["alto"], anuncio["url_archivo"], anuncio["url_clic"]))
            elif anuncio["formato"]=="Social": #y con social
                self.__anuncios.append(Social(anuncio["ancho"], anuncio["alto"], anuncio["url_archivo"], anuncio["url_clic"]))
    
    @property
    def nombre(self):#getter
        return self.__nombre
    @nombre.setter  #setter
    def nombre(self, nombre):
        if len(nombre) <=250: #validación del largo del nombre de la campaña
            self.__nombre = nombre
            return self.__nombre
        else: #si excede el límite se lanza un error específico del programa, al que se le ingresa un mensaje, los caracteres ingresados y el límite
            raise LargoExcedidoError("Error: El nombre excede el largo permitido.", len(nombre), 250)

    @property
    def fecha_inicio(self): #getter
        return self.__fecha_inicio
    @fecha_inicio.setter #setter
    def fecha_inicio(self, fecha_inicio:str):
        self.__fecha_inicio = fecha_inicio
        return self.__fecha_inicio
    
    @property
    def fecha_termino(self):  #getter
        return self.__fecha_termino
    @fecha_termino.setter #setter
    def fecha_termino(self, fecha_termino:str):
        self.__fecha_termino = fecha_termino
        return self.__fecha_termino
    
    @property
    def anuncios(self):  #getter
        return self.__anuncios
    
    def __str__(self) -> str: #sobrecarga de string
        contador_videos = 0  #variables para contar cada una de las instancias
        contador_display = 0
        contador_social = 0
        for anuncio in self.anuncios: #se recorre la lista de anuncios
            if isinstance(anuncio, Video): #si es instancia de video se suma 1 al contador
                contador_videos +=1
            elif isinstance(anuncio,Display): #si es instancia de display se suma 1 al contador
                contador_display +=1
            elif isinstance(anuncio, Social): #si es instancia de social se suma 1 al contador
                contador_social+=1
        #se elabora un retorno con todo el string para entregar cuando impriman una campaña    
        retorno = f"""
Nombre de la campaña: {self.nombre}
Anuncios: {contador_videos} Video , {contador_display} Display, {contador_social} Social
        """ #cada contador reporta cuántos objetos hay de cada clase
        return retorno
    