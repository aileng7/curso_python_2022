from Modulo2.TP.Botella import Botella
from Modulo2.TP.Viaje import Viaje


class Deposito:
    def __init__(self, balance: float, stock: list[Botella], viajes: list[Viaje]):
        self.__balance = balance
        self.__stock = stock
        self.__viajes = viajes

    def ingreso(self, gaseosas: list[Botella]) -> None:
        for gaseosa in gaseosas:
            self.__stock += gaseosa

    def egreso(self, gaseosas: list[Botella]) -> None:
        for gaseosa in gaseosas:
            self.__stock -= gaseosa

    def cierre_mensual(self) -> None:
        pass
