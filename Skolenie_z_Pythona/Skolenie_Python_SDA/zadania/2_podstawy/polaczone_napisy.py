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
    sstuoppermarket
    W przypadku kiedy jakis napis jest dluzszy, nalezy go po prostu
    przepisac, podobnie jak to zostalo pokazane na drugim przykladzie.
"""


def merge_strings( string1, string2 ):
    """Laczy naprzemiennie napisy string1 oraz string2.

    :param string1: pierwszy napis do polaczenia.
    :param string2: drugi napis do polaczenia.
    :return: napis zlozony z podanych jako argumenty.

    """
    res = []
    if len(string1) == len(string2):
        for i in range(len(string1)):
            res.append(string1[i] + string2[i])

    elif len(string1) > len(string2):
        for i in range(len(string2)):
            res.append(string1[i] + string2[i])
        res.append(string1[len(string2):])

    elif len(string1) < len(string2):
        for i in range(len(string1)):
            res.append(string1[i] + string2[i])
        res.append(string2[len(string1):])
    return "".join(res)


print(merge_strings("1234", "123456789"))
