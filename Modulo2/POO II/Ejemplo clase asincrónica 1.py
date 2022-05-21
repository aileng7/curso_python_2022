class Animal:
        esta_vivo = True

        def respirar(self) -> None:
            print("Inhalando...")
            print("Exhalando...")

class Perro(Animal):
    pass

boby = Perro()
boby.respirar()
print(boby.esta_vivo)