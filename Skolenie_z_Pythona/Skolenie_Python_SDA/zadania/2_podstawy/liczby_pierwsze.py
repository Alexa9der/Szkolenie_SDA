"""
    Napisz funkcje stwierdzajaca czy podana jako argument liczba
    jest liczba pierwsza czy nie. Liczba jest pierwsza, kiedy dzieli sie
    tylko przez siebie i przez 1. Jednym z algorytmow wyszukiwania liczb
    pierwszych jest sprawdzenie czy zadna z liczb od 2 do LICZBA-1
    (lub od 2 do pierwiastek z LICZBA) nie dzieli badanej liczby bez reszty.
    Uwaga: 0 i 1 nie sa zaliczane ani do liczb pierwszych, ani do zlozonych.
"""


def is_prime_number(number):
    """Sprawdza czy argument number jest liczba pierwsza.

    :param number: liczba typu int.
    :return: True jezeli liczba jest pierwsza,
             False jezeli jest zlozona.

    """
    res = True
    for i in range(3,number):
        if number % i == 0:
            res = False
    if number == 1 or number == 3 or number == 0 :
        res = True

    return res

print(is_prime_number(3))
