"""
    Stworz dekorator o nazwie twice, ktory wywola dwukrotnie funkcje opakowujaca.
    Przyklad, funkcja po opakowaniu wykona sie dwa razy:
    @twice
    def print_hello():
        print("hello")

    >> print_hello()
    hello
    hello

    @twice
    def print_bye():
        print("bye")

    >>print_bye()
    bye
    bye

    Przetestuj swoje rozwiazanie.
"""

from typing import Callable


# Przykladowe rozwianie 1
def twice(function: Callable) -> Callable:  # typ obiektu, na ktorym mozemy uzyc operatora wywolania, czyli nawiasow ()

    def inner(*args, **kwargs):
        function(*args, **kwargs)
        return function(*args, **kwargs)

    return inner


# Przykladowe rozwianie 2
def twice(function: Callable) -> Callable:  # typ obiektu, na ktorym mozemy uzyc operatora wywolania, czyli nawiasow ()

    def inner(*a, **k):
        function(*a, **k)
        returned_value = function(*a, **k)
        return returned_value

    return inner


@twice
def print_hello():
    print("hello")


@twice
def print_bye():
    print("bye")
