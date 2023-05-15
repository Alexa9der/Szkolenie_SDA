"""
    Napisz dwie niezalezne funkcje rozwiazujace nastepujace problemy:
    a) count_digits powinno zliczac ilosc cyfr w liczbie calkowitej,
       ktora zostanie podana jako argument,
    b) count_zeros powinno zliczac ilosc zer w liczbie calkowitej, ktora zostanie
       podana jako argument.
    Przyklady:
    >> x = count_digits(1234)
    >> print(x)
    4
    >> x = count_zeros(1000)
    >> print(x)
    3
    Zadania mozna rozwiazac w sposob "matematyczny", ale rowniez
    wykorzystujac uproszczenia Pythona.
    Podpowiedz: a gdyby tak liczbe rzutowac na napis?
"""

# Przykladowe rozwiazanie 1: rzutowanie na str i uzycie len

def count_digits(number):
    """Zlicza ilosc cyfr w liczbie.

    :param number: pewna liczba calkowita
    :return: ilosc cyfr w liczbie (int).

    """
    return len(str(number))


# Przykladowe rozwiazanie 1: rzutowanie na str i uzycie sum z "list comprehension"
# dla number = 1010 powstanie lista [1, 1] (bo za każde zero dodajemy 1 do nowej listy)
# ostatecznie sumujemy elementy listy -> w tym przypadku wyjdzie 2

def count_zeros(number):
    """Zlicza zera w liczbie number.

    :param number: pewna liczba calkowita
    :return:
    """
    return sum(1 for zero in str(number) if zero == "0")


# Przykladowe rozwiazanie 2: rzutowanie po str i iteracja po znakach

def count_zeros(number):
    """Zlicza zera w liczbie number.

    :param number: pewna liczba calkowita
    :return:
    """
    number = str(number)
    zeros_amount = 0
    for digit in number:
        if digit == "0":
            zeros_amount += 1

    return zeros_amount
