from campania import Campaña
from datetime import datetime

fecha_hora = datetime.now() #variable con datetime para después

anuncios = [{"formato":"Video",
            "ancho": 15,
            "alto": 15,
            "url_archivo": "url_archivo",
            "url_clic":"url_clic",
            "duracion": 50
            }] #lista con un diccionario como podrían estar los anuncios

campaña_demo = Campaña("Sonrisa Pepsodent","26 de Abril", "19 de Mayo", anuncios) #instancia de campaña que toma el diccionario y genera un anuncio de clase video

try: #manejo del error específico del programa que controla el largo del nombre
    campaña_demo.nombre = input("Ingrese el nuevo nombre para la campaña:\n")
except Exception as error:
    print(f"{error}\n")
    with open("dia13/prueba/logs/error.log", "a+",encoding="utf-8") as log:  #si hay una excepción se va a almacenar su mensaje  en un archivo error.log
        log.write(f"{fecha_hora.strftime("[%Y/%m/%d, %H:%M:%S]")} {error}\n")  #además del mensaje, se le va a agregar la fecha y hora del error (con formato)
        log.close() # cierre del archivo que se abrió para escribir el error
        
try: #mismo procedimiento con el otro error específico
    campaña_demo.anuncios[0].sub_tipo = input("Ingrese el nuevo sub-tipo para el anuncio:\n").lower()
except Exception as error:
    print(f"{error}\n")
    with open("dia13/prueba/logs/error.log", "a+",encoding="utf-8") as log:
        log.write(f"{fecha_hora.strftime("[%Y/%m/%d, %H:%M:%S]")} {error}\n")
        log.close()

campaña_demo.anuncios[0].mostrar_formatos()  #pruebas
campaña_demo.anuncios[0].comprimir_anuncio() #muchas pruebas
campaña_demo.anuncios[0].redimensionar_anuncio()
print(type(campaña_demo))
print(type(campaña_demo.anuncios[0]))
print(campaña_demo)

