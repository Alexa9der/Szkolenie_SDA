"""
    Napisz funkcje przyjmujaca dwa zbiory (sety) jako parametry
    i znajdujaca liczby, ktore znajduja sie zarowno w jednym zbiorze,
    jak i w drugim.
    Funkcja powinna zwrocic set powtarzajacych sie liczb. Jezeli zadna
    liczba sie nie powtarza, funkcja powinna zwrocic pusty zbior.
    Uwaga: w Pythonie pusty set (zbior) deklaruje sie tak:
    >> pusty = set()
    a nie tak:
    >> pusty = {} # w taki sposob deklaruje sie slownik.
    Zadanie powinno zostac wykonane w inny sposob niz za pomoca
    uzycia skladni:
    >> set1 & set2
    ktore w skrocie ustala czesc wspolna obu zbiorow.
"""

# Przykladowe rozwiazanie 1: pojedyncza petla i operator "in"


def find_common_numbers(set1, set2):
    """Znajduje wspolne liczby z odbydwoch zbiorow.

    :param set1: pierwszy zbior liczbowy.
    :param set2: drugi zbior liczbowy.
    :return: nowy set posiadajacy liczby, ktore wchodza w sklad zarowno
        zbioru set1 jak i zbioru set2.

    """
    commons = set()

    for number in set1:
        if number in set2:
            commons.add(number)

    return commons


# Przykladowe rozwiazanie 2: podwojna petla


def find_common_numbers(set1, set2):
    """Znajduje wspolne liczby z odbydwoch zbiorow.

    :param set1: pierwszy zbior liczbowy.
    :param set2: drugi zbior liczbowy.
    :return: nowy set posiadajacy liczby, ktore wchodza w sklad zarowno
        zbioru set1 jak i zbioru set2.

    """
    commons = set()

    for number1 in set1:
        for number2 in set2:
            if number1 == number2:
                commons.add(number1)  # albo commons.add(number2), to to samo

    return commons
