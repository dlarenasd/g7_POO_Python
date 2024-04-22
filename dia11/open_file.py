""" 
FUNCIÓN OPEN
open(ruta, argumento o modo de apertura) --> retornará un archivo de tipo file
"""
import os
try:
    log_file = open(os.path.abspath("dia11/logs/error.log")) #--> abspath: obtener la ruta absoluta de un archivo, sin escribir tooooda la ruta.
    print(log_file) #FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Bootcamp Python\\G7-0044-1\\Módulo_POO\\logs\\error.log'
    print(type(log_file)) #<class '_io.TextIOWrapper'> i = in/ o = out/ archivo de ingreso y salida
    #con carpeta incluida --> <_io.TextIOWrapper name='C:\\Bootcamp Python\\G7-0044-1\\Módulo_POO\\dia11\\logs\\error.log' mode='r' encoding='cp1252'>
except FileNotFoundError as fnfe:
        print("Error: Archivo o directorio no encontrado")
        print(fnfe)#[Errno 2] No such file or directory: 'C:\\Bootcamp Python\\G7-0044-1\\Módulo_POO\\dia11\\logs\\error2.log'
        
#ARGUMENTO r --> SOLO LECTURA
print("-----------------------READ--------------------------------- \n")    
log_file2 = open(os.path.abspath("dia11/html/index.html"),"r") #el modo de apertura no puede ir adentro del abspath
print(log_file2.read()) #muestra todo el contenido
log_file2.close() #luego de abrir el archivo, lo cierro
print("------------------------READLINE-------------------------------- \n")    
log_file3 = open(os.path.abspath("dia11/html/index.html"),"r") 
print(log_file3.readline()) # muestra una línea de código, trabaja con for y muestra línea por línea. Por defecto va a mostrar la primera
log_file3.close() #luego de abrir el archivo, lo cierro
print("------------------------READLINES-------------------------------- \n")    
log_file4 = open(os.path.abspath("dia11/html/index.html"),"r") 
print(log_file4.readlines()) # retorna una lista de cada una de las líneas de código como sus elementos
""" ['<!DOCTYPE html>\n', '<html lang="en">\n', '<head>\n', '    <meta charset="UTF-8">\n', '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n', '    <title>Document</title>\n', '</head>\n', '<body>\n', '    \n', '</body>\n', '</html>']
PS C:\Bootcamp Python\G7-0044-1\Módulo_POO> """
log_file3.close() #luego de abrir el archivo, lo cierro
print("------------------------WITH-------------------------------- \n")  
with open("dia11/html/index.html", "r") as archivo:
    # print(archivo) #<_io.TextIOWrapper name='dia11/html/index.html' mode='r' encoding='cp1252'>
    for linea in archivo:
        print(linea.strip()) #entrega el string quitando los saltos de línea adicionales y el tabulado

#ARGUMENTO w --> SOLO ESCRITURA//LA RUTA DEBE EXISTIR 
log_file5 = open(os.path.abspath("dia11/html/assets/css/style.css"),"w") 
log_file5.write("/* Esto es otro comentario */\n") #write va escribiendo todo a la derecha, por lo que se recomienda usar \n y \t
log_file5.write("* {\n\tmargin: 0px \n}") 
log_file5.close()

import time
try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open(f"dia11/logs/{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")
        
#para hacer uso de r+ (como reemplazo de w), el archivo DEBE existir
# with open(f"dia11/logs/{round(time.time())}.log", "r+") as log:
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#FileNotFoundError: [Errno 2] No such file or directory: 'dia11/logs/1713803234.log'