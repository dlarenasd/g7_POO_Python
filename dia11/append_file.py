from datetime import datetime #fecha y hora

try:
    now = datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    edad = int(input("Ingrese su edad:\n"))

except Exception as e:
    with open("dia11/logs/error.log", "a+") as log: #va a buscarlo, si no está se genera y lo abre en lectura/escritura -->se le da un alias
        log.seek(0) #posiciónate al principio
        print(log.read()) 
        now = datetime.now() #retorna la fecha y hora, con horas, minutos, segundos y milisegundos
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n") #se le da formato a la hora para quitar los milisegundos
        log.seek(3) #la posición no es con un índice, es con bytes (caracteres)
        print(log.read(40)) #cantidad de bytes a imprimir
    
