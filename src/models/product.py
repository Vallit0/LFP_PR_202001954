class Product:
    def __init__(self, name: str, price: float, units: int) -> None:
        self.name:  str = name 
        self.price: float = price
        self.units: int = units
        self.balance: float = int(self.units)*(float(self.price))
