class Persona():
    def __init__(self):
        self.celula = 13765890
    def mensaje(self):
        print("mensaje desde la clase Persona")

class Obrero():
    def __init__(self):
        self.__especialista = 1
    def mensaje(self):
        print("mensaje desde la clase obrero")

obrero_planta = Obrero()
obrero_planta.mensaje()