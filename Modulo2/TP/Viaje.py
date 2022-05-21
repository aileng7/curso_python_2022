from Modulo2.TP.Botella import Botella
from Modulo2.TP.TipoViajeInvalido import TipoViajeInvalido

class Viaje:
    def __init__(self, tipo: str, fecha: str, botellas: list[Botella]):
        self.__tipo = tipo
        self.__fecha = fecha
        self.__botellas = botellas

    def __es_valido_tipo(self, tipo: str) -> bool:
        return tipo == "Ingreso" or "Egreso"

    def __set_tipo(self tipo:str) ->None:
        if self.__es_valido_tipo(tipo):
            self.__tipo = tipo
        else:
            raise TipoViajeInvalido(f"El tipo de viaje {tipo} es inválido.")

    def calcular_precio_total(self) -> float:
        precio_total = 0
        for botella in self.__botellas:
            precio_total += botella.precio
        return precio_total
