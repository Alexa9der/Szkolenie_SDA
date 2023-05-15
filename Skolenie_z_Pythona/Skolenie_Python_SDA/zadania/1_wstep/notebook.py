"""
    Stwórz klasę Notebook, która będzie zawierała pola: producenta, cenę netto oraz pamięć RAM.
    Dopisz metody do obliczenia ceny brutto (+23% VAT) oraz zwiększenia ilości RAM-u.
"""


class Notebook:
    def __init__( self, manufacturer: str, net_price: int, arm_memory: int):
        self.manufacturer = manufacturer  # producenta
        self.net_price = net_price        # cenę netto
        self.arm_memory = arm_memory      # pamięć RAM

    def gross_price_calculation( self) -> int:
        gross_prices = self.net_price + (self.net_price / 100) * 23
        return gross_prices

    def add_ram( self) -> int:
        return self.arm_memory + 1


hp_elite_book = Notebook("hp", 500, 8)

print(f"manufacturer: {hp_elite_book.manufacturer}")
print(f"net price: {hp_elite_book.net_price}")
print(f"arm memory: {hp_elite_book.arm_memory}GB")
print(f"gross prices: {hp_elite_book.gross_price_calculation()}")
print(f"new arm memory: {hp_elite_book.add_ram()}")

