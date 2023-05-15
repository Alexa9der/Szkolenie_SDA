"""
    Zadanie polega na napisaniu funkcji zliczajacej ilosc
    parzystych liczb w liscie liczb podanej jako parametr funkcji.
    Funkcja nazywa sie count_even_number, natomiast parametr wejsciowy
    jest lista liczb o nazwie numbers.
    Napisz rozwiazanie, ktore przebada liste w poszukiwaniu liczb parzystych
    i przy kazdym znalezieniu takowej zwiekszy licznik zmiennej pomocniczej.
    Funkcja powinna zwracac ilosc liczb parzystych w podanej liscie.
    Zakladamy, ze lista bedzie dostarczana z programu, nie przez uzytkownika
    z wykorzystaniem funkcji input().
    Przyklad:
    >> list_of_numbers = [1, 2, 3, 4, 5, 6] -> 3 liczby parzyste: 2, 4, 6
    >> x = count_even_numbers(list_of_numbers)
    x powinno wynosic 3.
    Uwaga: 0 jest liczba parzysta.
"""

# Przykladowe rozwiazanie 1: list comprehension + wbudowana funkcja sum
# jezeli nie pamietasz jak dziala funkcja sum(), odsylam do dokumentacji Pythona :)

def count_even_numbers(numbers):
    """Zlicza liczby parzyste w liscie podanej jako argument.

    :param numbers: lista liczb.
    :return: ilosc liczb parzystych w podanej liscie, typ wartosci
        zwracanej to int.

    """
    return sum(1 for number in numbers if number % 2 == 0)


# Przykladowe rozwiazanie 2: iteracja po liscie liczb

def count_even_numbers(numbers):
    """Zlicza liczby parzyste w liscie podanej jako argument.

    :param numbers: lista liczb.
    :return: ilosc liczb parzystych w podanej liscie, typ wartosci
        zwracanej to int.

    """
    evens_amount = 0

    for number in numbers:
        if number % 2 == 0:
            evens_amount = evens_amount + 1

    return evens_amount


# Przykladowe rozwiazanie 3: iteracja po liscie liczb z wykorzystaniem continue
# jezeli liczba dzieli sie przez 2 z reszta, to nie zwiekszamy licznika
# tylko idziemy do nastepnego obiegu petli

def count_even_numbers(numbers):
    """Zlicza liczby parzyste w liscie podanej jako argument.

    :param numbers: lista liczb.
    :return: ilosc liczb parzystych w podanej liscie, typ wartosci
        zwracanej to int.

    """
    evens_amount = 0

    for number in numbers:
        if number % 2:
            continue
        evens_amount += 1

    return evens_amount
