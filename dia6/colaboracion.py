class Superficie():
    def __init__(self):
        self.__resistencia = 2
    @property
    def resistencia(self):
        return self.__resistencia
class Pelota():
    def rebotar(self, altura: float):
# Se instancia la clase que colabora con Pelota
        s = Superficie()
        rebotes = []
        while altura > 0:
            rebotes.append(altura)
            rebotes.append(0)
    # La instancia de Superficie colabora con Pelota para rebotar
            altura //= s.resistencia
        return rebotes
p = Pelota()
# Salida: [10, 0, 5, 0, 2, 0, 1, 0]
print(p.rebotar(10))