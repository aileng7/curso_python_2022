class Domicilio:
    def __init__(self):
        self.__street = " "
        self.__number = " "
        self.__city = " "

    def insert_street(self, street: str):
        self.__street = street

    def insert_number(self, number: str):
        self.__number = number

    def insert_city(self, city: str):
        self.__city = city

    def address(self) -> str:
        return f"{self.__street} {self.__number} {self.__city}"


def print_address():
    print(Domicilio)


class Persona:
    def __init__(self):
        self.__name = " "
        self.__last_name = " "
        self.__address = " "

    def insert_name(self, name: str) -> None:
        self.__name = name

    def insert_last_name(self, last_name: str) -> None:
        self.__last_name = last_name

    def full_name(self) -> str:
        return f"{self.__name} {self.__last_name}"

    def insert_address(self, address: Domicilio):
        self.__address = address

    def address(self):
        return f"{self.__address}"
