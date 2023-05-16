"""
    Napisz program, który pobiera od użytkownika słowo, a następnie wyświetla słowo złożone z co drugiego znaku pobranego.
    W drugiej kolejności program powinien wyświetlić słowo z pozostałych liter.
"""

word = "12345" # input("Podaj slowo:\n")
print(word[1::2])
print(word[0::2])