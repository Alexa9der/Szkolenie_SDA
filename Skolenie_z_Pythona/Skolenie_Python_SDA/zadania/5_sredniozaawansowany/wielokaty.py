"""
    Na podstawie klasy abstrakcyjnej Wielokat, stworz 3 klasy dziedziczace: Kwadrat, Prostokat, Trojkat.
    Kazda z tych klas musi byc konkretna (a nie abstrakcyjna), powinna wiec nadpisywac wszystkie metody
    abstrakcyjne z klasy Wielokat. Kazda konkretna klasa powinna miec definicje konstruktora __init__
    (dla przykładu obiekt typu Kwadrat, powinien miec jeden atrybut self.bok, obiekt prostokat dwa atrybuty:
    self.bok1, self.bok2, a trojkat self.bok, self.wysokosc).
    Na koniec stworz funkcje zarzadzajaca obiektami stworzonych klas, ktora w petli bedzie obliczala pola
    dla kazdego obiektu.
"""

from abc import ABC  # Python отсутствует встроенная поддержка абстрактных классов,
                     # для этой цели используется модуль abc (Abstract Base Class)
from abc import abstractmethod  # абстрактный метод, который будет необходимо переопределять для каждого подкласса
from typing import Union  # Union sugeruje co moze zwrocic funkcja


class Wielokat(ABC):

    @abstractmethod
    def oblicz_pole( self ) -> Union[int, float]:  # Union sugeruje ze funkcja moze zwrocic inta albo floata
        """Metoda ma za zadanie obliczyc pole danego obiektu.

        Ze wzgledu na fakt, iz nie wiemy w tym momencie jaki to jest wielokat,
        nie potrafimy obliczyc jego pola. Do redefinicji w klasie dziedziczacej.

        :return: wartosc pola jako liczba calkowita lub wymierna.
        """
        ...


class Kwadrat(Wielokat):
    def __init__( self, bok ):
        self.bok = bok

    def oblicz_pole( self ) -> Union[int, float]:
        return self.bok ** 2


class Prostokat(Wielokat):
    def __init__( self, bok1, bok2 ):
        self.bok1 = bok1
        self.bok2 = bok2

    def oblicz_pole( self ) -> Union[int, float]:
        return self.bok1 * self.bok2


class Trojkat(Wielokat):
    def __init__( self, bok, wysokosc ):
        self.bok = bok
        self.wysokosc = wysokosc

    def oblicz_pole( self ) -> Union[int, float]:
        return (1 / 2) * (self.bok * self.wysokosc)


def licz_pola( wielokaty: list ) -> list:
    """Oblicza pola wszystkich wielokatow podanych w liscie.

    :param wielokaty: lista obiektow dziedziczacych po Wielokat.
    :return: lista obliczonych pol.

    """
    return [i.oblicz_pole() for i in wielokaty]


def mean():
    kwadrat = Kwadrat(4)
    prostokat = Prostokat(4, 4)
    trojkat = Trojkat(4, 4)

    print(licz_pola([kwadrat, prostokat, trojkat]))


if __name__ == "__main__":
    mean()
