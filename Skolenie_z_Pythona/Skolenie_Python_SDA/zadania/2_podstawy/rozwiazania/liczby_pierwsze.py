"""
    Napisz funkcje stwierdzajaca czy podana jako argument liczba
    jest liczba pierwsza czy nie. Liczba jest pierwsza, kiedy dzieli sie
    tylko przez siebie i przez 1. Jednym z algorytmow wyszukiwania liczb
    pierwszych jest sprawdzenie czy zadna z liczb od 2 do LICZBA-1
    (lub od 2 do pierwiastek z LICZBA) nie dzieli badanej liczby bez reszty.
    Uwaga: 0 i 1 nie sa zaliczane ani do liczb pierwszych, ani do zlozonych.
"""

# Przykladowe rozwiazanie 1: petla od 2 do LICZBA-1


def is_prime_number(number):
    """Sprawdza czy argument number jest liczba pierwsza.

    :param number: liczba typu int.
    :return: True jezeli liczba jest pierwsza,
             False jezeli jest zlozona.

    """
    if number in (0, 1):
        return False

    for i in range(2, number-1):
        if number % i == 0:
            return False

    return True


# Przykladowe rozwiazanie 2: petla od 2 do pierwiastka z LICZBA-1
# zgodnie z matematyka - wystarczy sprawdzic dzielniki do pierwiastka z LICZBA-1
# math.ceil() i math.sqrt() to funkcje z modulu math, polecam zajrzec do dokumentacji Pythona :)
# math.ceil(x) - zaokragla x w gore, math.sqrt(x) oblicza pierwiastek z x

import math


def is_prime_number(number):
    """Sprawdza czy argument number jest liczba pierwsza.

    :param number: liczba typu int.
    :return: True jezeli liczba jest pierwsza,
             False jezeli jest zlozona.

    """
    if number == 0 or number == 1:
        return False

    for i in range(2, math.ceil(math.sqrt(number-1))):
        if number % i == 0:
            return False

    return True
