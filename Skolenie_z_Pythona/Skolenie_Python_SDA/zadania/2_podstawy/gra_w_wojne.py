"""
    Stworz prosty symulator gry karcianej wojna.
    Zadaniem Twojej funkcji jest wskazanie, ktora karta
    zwyciezy. Parametrami sa znaki card1 oraz card2.
    Moga one przyjmowac wartosci:
    <"1", "2", "3", ..., "10", "J", "D", "K", "A"> - wielkosc
    liter bedzie miala znaczenie (choc mozna przedstawic rozwiazanie,
    w ktorym nie bedzie znaczylo czy litera jest duza czy mala).
    Funkcja powinna zwracac liczbe 1, jezeli wygra gracz 1,
    2 - jezeli zwyciezy gracz 2 lub 0 jesli karty sa takie same.
    Przyklady:
    >> determine_the_winner("5", "2")
    1
    >> determine_the_winner("D", "A")
    2
    >> determine_the_winner("K", "8")
    1
    >> determine_the_winner("4", "4")
    0
"""


def determine_the_winner( card1, card2 ):
    """Wskazuje zwyciezce potyczki w grze wojna.

    :param card1: litera (string) reprezentujaca karte gracza 1.
    :param card2: litera (string) reprezentujaca karte gracza 2.
    :return: 0 dla remisu, 1 jesli zwyciezy gracz 1, 2 dla zwyciestwa gracza 2.

    """
    res = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'D': 12, 'K': 13, 'A': 14}
    card1 = card1.upper()
    card2 = card2.upper()

    if res[card1] > res[card2]:
        return 1
    elif res[card1] < res[card2]:
        return 2
    else:
        return 0


print(determine_the_winner("D", "A"))

