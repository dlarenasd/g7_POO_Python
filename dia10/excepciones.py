class Error(Exception):
    pass
class DivisorError(Error):
    def __init__(self, mensaje, divisor: int):
        self.mensaje = mensaje
        self.divisor = divisor

class MisExcepciones(Exception):
    def imprimir_promedio(self,dividendo,divisor):
        try:
            promedio=dividendo/divisor
            print(f"El promedio es: {promedio}")
            
        except ZeroDivisionError:
            print("ERROR: El divisor no puede ser un cero")
        #captura genérica de una excepción
        except Exception as error:
            print("ERROR: Se ha producido un error:", error)
        
        finally: #EL FINALLY SIEMPRE SE VA A EJECUTAR, CON EXCEPCIONES O NO. CUIDADO
            print("El método se ha ejecutado \n")
    
calculo_promedio = MisExcepciones()

"""
try:
    dividendo = int(input("Ingrese el número del dividendo: "))
    divisor = int(input("Ingrese el número del divisor: "))
    calculo_promedio.imprimir_promedio(dividendo, divisor)
except ValueError:
    print("Error en el ingreso de los datos")
    
"""
valido=True
while valido:
    try:
        dividendo = int(input("Ingrese el número del dividendo: ")) #se puede dividir el bloque de validación
        valido = False
    except ValueError:
        print("Error en el ingreso del dividendo")

valido=True
while valido:
    try:
        divisor = int(input("Ingrese el número del divisor: "))
        if divisor == 0: #validar con otron control de errores de una clase
            raise DivisorError("el divisor no puede ser cero.", divisor) #mensaje de error
        valido = False
    except DivisorError as dError:
        print("Error en el ingreso del divisor:", dError.mensaje)
    except ValueError:
        print("Error en el ingreso del divisor")
        
#calculo_promedio.imprimir_promedio(100,0) #ZeroDivisionError: division by zero // Se ha producido un error: division by zero
#calculo_promedio.imprimir_promedio(100,"0") #Se ha producido un error: unsupported operand type(s) for /: 'int' and 'str'
calculo_promedio.imprimir_promedio(dividendo,divisor)
