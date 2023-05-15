"""
    Napisz funkcje, ktorej zadaniem jest podwojenie kazdego znaku
    w napisie podanym jako parametr wejsciowy.
    Dla przykladu, wartoscia zwrocona z funkcji produce_double_sings
    przy argumencie "Python", powinno byc slowo "PPyytthhoonn".
    Kazda litera powinna byc podwojona zachowujac swoja wielkosc.
    Rozpatrujemy tylko napisy jednoslowowe.
"""

# Przykladowe rozwiazanie 1: korzystamy z funkcji join, ktora laczy kazdy element
# z listy w string; elementy sa rozdzielane tym, co stoi po lewej stronie join,
# w naszym przypadku niczym, bo mamy pusty string ""
# dla listy [1, 2, 3] i stringa "-" na ktorym wolamy joina, wywolanie bedzie wygladac:
# >> "-".join([1, 2, 3])
# a wynik:
# >> "1-2-3"
# zachecam do sprawdzenia dokumentacji! :)


def produce_double_signs(string):
    """Tworzy nowy napis na podstawie podanego, podwajajac kazdy znak.

    :param string: napis, w ktorym znaki powinny byc podwojone
    :return: nowy napis z podwojonymi znakami.

    """
    return "".join(sign*2 for sign in string)  # przypomnienie: mnozenie stringa podwoi go


# Przykladowe rozwiazanie 2: iteracja i podwojenie

def produce_double_signs(string):
    """Tworzy nowy napis na podstawie podanego, podwajajac kazdy znak.

    :param string: napis, w ktorym znaki powinny byc podwojone
    :return: nowy napis z podwojonymi znakami.

    """
    new_string = ""

    for sign in string:
        new_string += sign
        new_string += sign

    return new_string
