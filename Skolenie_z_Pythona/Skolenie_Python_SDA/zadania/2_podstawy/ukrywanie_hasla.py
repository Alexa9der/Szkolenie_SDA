"""
    Napisz prosta funkcje "szyfrujaca". Jej zadaniem jest zamiana
    co trzeciego znaku w hasle na znak gwiazdki (*).
    Przyklad:
    >> x = hide_password("moje_super_tajne_haslo123")
    >> print(x)
    "mo*e_*up*r_*aj*e_*as*o1*3"
    Pamietaj, ze dlugosc napisu nie musi byc podzielna przez 3.
"""


def hide_password( password ):
    """Ukrywa co trzecia litere w hasle password.

    :param password: haslo z gwiazdkami co trzecia litere.
    :return: napis z czesciowo ukrytym haslem.

    """
    res = []
    for i in range(1, len(password) + 1):
        if i % 3 == 0:
            res.append("*")
        else:
            res.append(password[i - 1])
    return "".join(res)

print(hide_password("moje_super_tajne_haslo123"))
print(hide_password("moje_super_tajne_haslo123") == "mo*e_*up*r_*aj*e_*as*o1*3")
