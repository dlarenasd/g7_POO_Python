from error import HoraError, LargoTextoError, FechaError
from reunion import Reunion
import re
titulo = None
hora = None
fecha = None
time_re = "^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$"
date_re = "^([0-3]?\d\/{1})([01]?\d\/{1})([12]{1}\d{3}?)$"

while True:
    try:
        if titulo is None or len(titulo) > 150:
            titulo = input("\nIngrese título de la reunión" " (Máximo 150 caracteres):\n")
            
            if len(titulo) > 150:
                raise LargoTextoError("Título de la reunión excede máximo de caracteres", titulo, 150)
        if hora is None or re.search(time_re, hora) is None:
            hora = input("\nIngrese hora de la reunión" " (Formato: HH:MM:SS):\n")
        if fecha is None or re.search(date_re, fecha) is None:
            fecha = input("\nIngrese fecha de la reunión" " (Formato: DD/MM/AAAA):\n")

        if re.search(time_re, hora) is None:
            raise HoraError("Formato de Hora debe ser HH:MM:SS.")
        if re.search (date_re, fecha) is None:
            raise FechaError("Formato de Fecha debe ser DD/MM/AAAA.")
    except Exception as e:
        print(f"\n{e}\n")
        continue
    else:
        break

r = Reunion(titulo, hora, fecha)
print("\nReunión creada correctamente.")
