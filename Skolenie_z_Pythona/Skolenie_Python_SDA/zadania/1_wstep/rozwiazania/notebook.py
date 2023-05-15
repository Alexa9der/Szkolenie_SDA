"""
    Stwórz klasę Notebook, która będzie zawierała pola: producenta, cenę netto oraz pamięć RAM.
    Dopisz metody do obliczenia ceny brutto (+23% VAT) oraz zwiększenia ilości RAM-u.
"""

class Notebook:
    VAT = 23

    def __init__(self, manufacturer, nett_price, ram):
        self.manufacturer = manufacturer
        self.nett_price = nett_price
        self.ram = ram

    @property
    def gross_price(self):
        return self.nett_price * (1 + self.VAT/100)

    def expand_ram(self, extra_ram):
        self.ram += extra_ram


if __name__ == '__main__':

    my_notebook = Notebook('msi', 3300, 16)
    print(f'Your {my_notebook.manufacturer} has '
          f'{my_notebook.ram} GB of RAM.')
    extra_ram = int(input('Add extra RAM: '))
    my_notebook.expand_ram(extra_ram)
    print(f'Your {my_notebook.manufacturer} has '
          f'{my_notebook.ram} GB of RAM.')
