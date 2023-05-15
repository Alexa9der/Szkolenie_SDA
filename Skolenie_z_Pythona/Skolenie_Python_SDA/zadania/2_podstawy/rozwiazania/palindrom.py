"""
    Napisz funkcje sprawdzajaca czy napis podany jako argument do niej
    jest palindromem. Palindrom to napis, ktory czytany od lewej
    do prawej brzmi tak samo jak czytany od prawej do lewej, np kajak.
    Dla ulatwienia zaloz, ze napis bedzie zawsze jednym slowem.
    Zakladamy, ze pusty string jest palindromem.
"""

# Przykladowe rozwiazanie 1: korzytamy z dobrodziejstw Pythona


def check_if_palindrome(string):
    """Sprawdza czy podany string (jedno slowo) jest palindromem.

    :param string: napis do sprawdzenia.
    :return: True jezeli napis jest palindromem,
             False w przeciwnym wypadku.

    """
    return string == string[::-1]


# Przykladowe rozwiazanie 2: porownujemy kolejno znaki
# index 0 z indeksem -1
# index 1 z indeksem -2 itd.


def check_if_palindrome(string):
    """Sprawdza czy podany string (jedno slowo) jest palindromem.

    :param string: napis do sprawdzenia.
    :return: True jezeli napis jest palindromem,
             False w przeciwnym wypadku.

    """
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return False
    return True
