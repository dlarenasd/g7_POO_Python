from pelota import Pelota

nueva_pelota= Pelota("Negro")
nueva_pelota.__password= "admin1234"
#print(nueva_pelota.__password)

nueva_pelota.setColor("Blanco")  #asignar color mediante un método
print(nueva_pelota.color)

nueva_pelota.color = "Naranjo"  #asignar color mediante un setter
print(nueva_pelota.color)

#nueva_pelota.color = ""
#print(nueva_pelota.color)  #asignación de color por medio de validación en el setter

nueva_pelota.color
print(nueva_pelota.color)