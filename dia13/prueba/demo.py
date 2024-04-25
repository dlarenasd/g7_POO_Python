from campania import Campaña
from datetime import datetime
from error import SubTipoInvalidoError, LargoExcedidoError

fecha_hora = datetime.now() #variable con datetime now para después

anuncios = [{"FORMATO":"Video",
            "ancho": 15,
            "alto": 15,
            "url_archivo": "url_archivo",
            "url_clic":"url_clic",
            "duracion": 50,
            "sub_tipo" : "instream"
            }] #lista con un diccionario como planteé que iba a estar la información para instanciar anuncios

campaña_demo = Campaña("Sonrisa Pepsodent","26 de Abril", "19 de Mayo", anuncios) #instancia de campaña que toma el diccionario y genera un anuncio de clase video

try: #manejo del error específico del programa que controla el largo del nombre
    campaña_demo.nombre = input("Ingrese el nuevo nombre para la campaña:\n")
except LargoExcedidoError as error:
    print(f"ERROR: El largo ingresado excede el máximo. \n")
    with open("dia13/prueba/logs/error.log", "a+",encoding="utf-8") as log:  #si hay una excepción se va a almacenar su mensaje  en un archivo error.log
        log.write(f"{fecha_hora.strftime("[%Y/%m/%d, %H:%M:%S]")} ERROR: El largo ingresado excede el máximo. {type(error)}\n")  #además del mensaje, se le va a agregar la fecha y hora del error (con formato)
        log.close() # cierre del archivo que se abrió para escribir el error
        
try:#manejo del error específico del programa que controla si el subtipo ingresado corresponde a los posibles
    campaña_demo.anuncios[0].sub_tipo = input(f"Ingrese el nuevo sub-tipo para el anuncio: [disponibles: {campaña_demo.anuncios[0].SUB_TIPOS[0]} y {campaña_demo.anuncios[0].SUB_TIPOS[1]}] \n").lower()
except SubTipoInvalidoError as error:
    print(f"ERROR: El sub-tipo ingresado no corresponde con este anuncio. \n")
    with open("dia13/prueba/logs/error.log", "a+",encoding="utf-8") as log:  #si hay una excepción se va a almacenar su mensaje  en un archivo error.log
        log.write(f"{fecha_hora.strftime("[%Y/%m/%d, %H:%M:%S]")} ERROR: El sub-tipo ingresado no corresponde con este anuncio. {type(error)}\n")  #además del mensaje, se le va a agregar la fecha y hora del error (con formato)
        log.close() # cierre del archivo que se abrió para escribir el error
        


campaña_demo.anuncios[0].mostrar_formatos()  #pruebas
campaña_demo.anuncios[0].comprimir_anuncio() #muchas pruebas
campaña_demo.anuncios[0].redimensionar_anuncio()
print(type(campaña_demo))
print(type(campaña_demo.anuncios[0]))
print(campaña_demo)

""" PRUEBAS CON UNA LISTA DE DICCIONARIOS MÁS GRANDE

varios_anuncios = [{"FORMATO":"Video",
            "ancho": 15,
            "alto": 15,
            "url_archivo": "url_archivo",
            "url_clic":"url_clic",
            "duracion": 50,
            "sub_tipo" : "instream"},
            {"FORMATO":"Video",
            "ancho": 15,
            "alto": 15,
            "url_archivo": "url_archivo",
            "url_clic":"url_clic",
            "duracion": 50,
            "sub_tipo" : "outstream"},
            {"FORMATO":"Display",
            "ancho": 15,
            "alto": 15,
            "url_archivo": "url_archivo",
            "url_clic":"url_clic",
            "sub_tipo" : "tradicional"},
            {"FORMATO":"Social",
            "ancho": 15,
            "alto": 15,
            "url_archivo": "url_archivo",
            "url_clic":"url_clic",
            "sub_tipo" : "linkedin"},
            {"FORMATO":"Video",
            "ancho": 15,
            "alto": 15,
            "url_archivo": "url_archivo",
            "url_clic":"url_clic",
            "duracion": 50,
            "sub_tipo" : "instream"
            },{"FORMATO":"Social",
            "ancho": 15,
            "alto": 15,
            "url_archivo": "url_archivo",
            "url_clic":"url_clic",
            "sub_tipo" : "facebook"
            },{"FORMATO":"Display",
            "ancho": 15,
            "alto": 15,
            "url_archivo": "url_archivo",
            "url_clic":"url_clic",
            "sub_tipo" : "native"
            }]

campaña_prueba = Campaña("Probando, probando. Ahora serán varias", "hoy", "mañana", varios_anuncios)
campaña_prueba.anuncios[0].mostrar_formatos()  #pruebas
campaña_prueba.anuncios[1].comprimir_anuncio() #muchas pruebas
campaña_prueba.anuncios[2].redimensionar_anuncio()
print(type(campaña_prueba))
print(type(campaña_prueba.anuncios[3]))
print(len(campaña_prueba.anuncios))
print(campaña_prueba)

"""