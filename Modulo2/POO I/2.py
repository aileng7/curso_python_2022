class TarjetaDeCredito:
    def __init__(self, number: str, titular: str, buy_limit: float, available_limit: float):
        self.__number = number
        self.customer = titular
        self.buy_limit = buy_limit
        self.available_limit = available_limit

    def __can_buy(self, amount: float) -> bool:
        return amount <= self.available_limit

    def buy(self, amount: float) -> bool:
        if self.__can_buy(amount):
            self.available_limit -= amount
            return True
        return False

    def new_limit(self, new_limit: float) -> None:
        if new_limit < self.buy_limit:
            self.available_limit = new_limit
