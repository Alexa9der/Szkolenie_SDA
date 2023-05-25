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


def find_common_numbers( set1, set2 ):
    """Znajduje wspolne liczby z odbydwoch zbiorow.

    :param set1: pierwszy zbior liczbowy.
    :param set2: drugi zbior liczbowy.
    :return: nowy set posiadajacy liczby, ktore wchodza w sklad zarowno
        zbioru set1 jak i zbioru set2.

    """
    res1 = [i for i in set1 if i in set2]
    res2 = [i for i in set2 if i in set1]
    return {*res1, *res2}


set1 = {1, 2, 3, 4, 5}
set2 = {11, 12, 13, 14, 15}

print(find_common_numbers(set1, set2))
