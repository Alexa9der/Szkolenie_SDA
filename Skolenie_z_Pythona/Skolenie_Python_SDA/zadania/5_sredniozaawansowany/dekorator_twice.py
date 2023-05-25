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

from typing import Callable  # typ obiektu, na ktorym mozemy uzyc operatora wywolania, czyli nawiasow ()


def twice( repetitions=2 ) -> Callable:
    def decorators( function ):
        def wraper( *args, **kwargs ):
            res = [function(*args, **kwargs) for _ in range(repetitions)]
            return res
        return wraper
    return decorators


@twice(2)
def print_hello():
    print("hello")


@twice(repetitions=3)
def print_bye():
    print("bye")


def main():
    print_hello()
    print_bye()


if __name__ == "__main__":
    main()

