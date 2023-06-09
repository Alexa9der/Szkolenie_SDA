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


def count_digits(number):
    """Zlicza ilosc cyfr w liczbie.

    :param number: pewna liczba calkowita
    :return: ilosc cyfr w liczbie (int).

    """
    return len(list(str(number)))


def count_zeros(number):
    """Zlicza zera w liczbie number.

    :param number: pewna liczba calkowita
    :return:
    """
    num = list(str(number))
    count = 0

    for i in num :
        if i == "0":
            count += 1
    return count


print(count_digits(1234))
print()
print(count_zeros(1000))