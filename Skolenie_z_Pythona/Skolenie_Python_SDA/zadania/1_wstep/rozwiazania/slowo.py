"""
    Napisz program, który pobiera od użytkownika słowo, a następnie wyświetla słowo złożone z co drugiego znaku pobranego.
    W drugiej kolejności program powinien wyświetlić słowo z pozostałych liter.
"""

if __name__ == '__main__':
    word = input('Word? ')
    print(word[::2])
    print(word[1::2])
