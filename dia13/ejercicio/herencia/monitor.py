from televisor import Televisor

class Monitor():
    def __init__(self, resolucion):
        self.resolucion = resolucion
        
class MonitorLED (Monitor):
    pass

class MonitorMultifuncion(Monitor, Televisor):
    pass