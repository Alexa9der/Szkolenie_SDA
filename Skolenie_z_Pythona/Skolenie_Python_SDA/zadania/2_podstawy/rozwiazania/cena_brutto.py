"""
    Napisz funkcje, ktora na podstawie podanego slownika
    z zakupami jako kluczami oraz z krotka (tuple) z cena i podatkiem,
    wyliczy kwote brutto calych zakupow.
    Parametr grocery_list moze miec postac:
    {"mleko": (5.00, 10), "ser": (4.50, 15), "jogurt": (3, 25)}.
    Pierwsza wartosc w krotce to cena netto, druga to podatek (np. dla 10%
    podatku danego produktu i jego ceny brutto 10 pln, cena brutto bedzie
    wynosila 1.1*10). Nalezy zsumowac ceny brutto dla kazdego produktu
    i zwrocic wynik.
    Nalezy przyjac, ze uzytkownik nie poda blednych wartosci (czyli, ze
    cena nigdy nie bedzie ujemna, a podatek zawsze bedzie sie miescil
    w zbiorze <0; 100>.
"""

# Przykladowe rozwiazanie 1: korzystamy z funkcji wbudowanej sum

def calculate_brutto_prize(grocery_list):
    """Oblicza cene brutto wszystkich zakupow z grocery_list.

    :param grocery_list: slownik, w ktorym kluczami sa stringi reprezentujace zakupy,
        a wartosciami krotki (tuple) z dwiema liczbami: cena produktu i jego podatkiem.
    :return: sume wszystkich wartosci brutto z listy (jako liczba).

    """
    return sum(prize+prize*tax*0.01 for prize, tax in grocery_list.values())


# Przykladowe rozwiazanie 2: iterujemy w petli for po kluczach (!)

def calculate_brutto_prize(grocery_list):
    """Oblicza cene brutto wszystkich zakupow z grocery_list.

    :param grocery_list: slownik, w ktorym kluczami sa stringi reprezentujace zakupy,
        a wartosciami krotki (tuple) z dwiema liczbami: cena produktu i jego podatkiem.
    :return: sume wszystkich wartosci brutto z listy (jako liczba).

    """
    prize = 0
    for product in grocery_list:
        prize += grocery_list[product][0] + (grocery_list[product][0] * grocery_list[product][1] * 0.01)
    return prize


# Przykladowe rozwiazanie 3: iterujemy w petli for po watosciach, czyli po tuplach

def calculate_brutto_prize(grocery_list):
    """Oblicza cene brutto wszystkich zakupow z grocery_list.

    :param grocery_list: slownik, w ktorym kluczami sa stringi reprezentujace zakupy,
        a wartosciami krotki (tuple) z dwiema liczbami: cena produktu i jego podatkiem.
    :return: sume wszystkich wartosci brutto z listy (jako liczba).

    """
    prize = 0
    for product in grocery_list.values():
        prize += product[0] + (product[0] * product[1] * 0.01)
    return prize
