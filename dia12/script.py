from usuario import Usuario
import json
from datetime import datetime


lista_usuarios = [] #lista vacía para almacenar instancias
try:
    with open("dia12/usuarios.txt", "r") as usuarios: #abrir archivo en modo lectura con un alias
        for linea in usuarios.readlines(): #recorrer por línea el archivo con todas sus líneas
            try: #control de excepciones
                datos_linea = json.loads(linea) #convertir línea de texto en diccionario y guardarlo en una variable
                #se crea una instancia de Usuario con los parámetros desde datos_linea y se almacenan en lista_usuarios
                lista_usuarios.append(Usuario(datos_linea.get("nombre"), datos_linea.get("apellido"), datos_linea.get("email"), datos_linea.get("genero")))
            except Exception as e: #en caso de haber un error se le da un alias
                with open(f"dia12/logs/error_usuario.log", "a+",encoding="utf-8") as usuariolog: #y se escribe en error.log cuál fue el error
                    fecha_hora = datetime.now() #generamos una variable que contendrá la hora
                    usuariolog.write(f"{fecha_hora.strftime("[%Y/%m/%d, %H/%M/%S]")} Error al procesar la línea: {linea}\tExcepción: {e}\n")
                    #a esa hora se le da formato y se incluye al mensaje
                    usuariolog.close()
                print("Ha habido un error:", e ) #también se imprime dicho error por consola
            else:
                print(f"Usuario creado: {datos_linea.get("nombre")} {datos_linea.get("apellido")}") #si no hay errores, imprime el usuario creado con su nombre y apellido
    usuarios.close()
except Exception as error: #prueba, en caso de no estar el archivo lanza este error
    with open(f"dia12/logs/error_archivo.log", "a+",encoding="utf-8") as archivolog:
        archivolog.write(f"Error al abrir el archivo.\n\tExcepción: {error}\n")
    archivolog.close()









