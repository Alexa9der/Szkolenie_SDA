"""
    Napisz funkcje laczaca ze soba dwa napisy w sposob:
    najpierw pierwsza litera pierwszego napisu, potem pierwsza litera
    drugiego, druga litera drugiego napisu, itd...
    Funkcja powinna zwrocic nowy napis bedacy polaczeniem tych podanych
    jako parametry. Uwaga: wejsciowe napisy nie musza byc tej samej
    dlugosci!
    Przyklad:
    >> merge_strings("pies", "buda")
    pbiuedsa
    >> merge_strings("stop", "supermarket)
    sstuoopermarket
    W przypadku kiedy jakis napis jest dluzszy, nalezy go po prostu
    przepisac, podobnie jak to zostalo pokazane na drugim przykladzie.
"""

# Przykladowe rozwiazanie 1: iteracja po kazdym znaku i laczenie
# wczesniej dobieramy wspolna dlugosc i ewentualny koniec stringu
# jezeli ktorys z napisow jest dluzszy od drugiego


def merge_strings(string1, string2):
    """Laczy naprzemiennie napisy string1 oraz string2.

    :param string1: pierwszy napis do polaczenia.
    :param string2: drugi napis do polaczenia.
    :return: napis zlozony z podanych jako argumenty.

    """
    new_string = ""
    end_of_string = ""
    common_length = len(string1)

    if len(string1) > len(string2):
        end_of_string = string1[len(string2):]
        common_length = len(string2)
    elif len(string1) < len(string2):
        end_of_string = string2[len(string1):]

    for i in range(common_length):
        new_string += string1[i] + string2[i]

    return new_string + end_of_string
