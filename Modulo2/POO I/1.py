class Persona:
    def __init__(self, name: str, lastname: str) -> None:
        self.__name = name
        self.__lastname = lastname

    def fullname(self):
        return self.__name + " " + self.__lastname

    def initials(self):
        return self.__name[0] + "." + self.__lastname[0] + "."


ailen = Persona("Ailén", "González")
