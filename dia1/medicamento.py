class Medicamento():
    #atributos de clase
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_a_cero(numero:int):
        return numero > 0
    
    @staticmethod
    def modificar_atributo():
        Medicamento.IVA = 0.19 #este método modifica la clase, no el atributo del objeto
        