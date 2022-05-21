class Automovil:
    def __init__(self, mark: str, model: str, patent: str, fuel_capacity: float, amount_fuel: float, liter_km: float):
        self.mark = mark
        self.model = model
        self.patent = patent
        self.fuel_capacity = fuel_capacity
        self.amount_fuel = amount_fuel
        self.liter_km = liter_km

    def travel(self, km: float) -> bool:
        return self.amount_fuel > (km * self.liter_km)

    def __check_fuel_quantity(self, check_fuel_quantity: float) -> bool:
        return self.fuel_capacity >= (self.amount_fuel + check_fuel_quantity)

    def refuel(self, fuel_quantity: float) -> bool:
        if self.__check_fuel_quantity(fuel_quantity):
            self.amount_fuel += fuel_quantity
            return True
        return False
