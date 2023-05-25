"""
    Stworz klase Ulamek reprezentujaca liczby ulamkowe.
    Kazdy obiekt typu Ulamek powinien miec dwa atrybuty: self.licznik oraz self.mianownik.
    Glownym celem zadania jest dorobienie imlementacji, dzieki ktorej mozliwe stanie sie
    dodawanie, mnozenie, dzielenie i odejmowanie od siebie dwoch obiektow typu Ulamek. W tym celu nalezy
    przeladowac operatory +, -, *, / (magiczne metody: __add__, __sub__, __mul__, __truediv__).
    Pamietac trzeba o tym, ze przed dodaniem ulamkow, nalezy je sprowadzic do wspolnego mianowanika!
    Dla uproszczenia: nie trzeba skracac ulamkow, czyli ulamka 10/20 nie trzeba bedzie sprowadzac do postaci 1/2.
    Takie dzialania powinny sie zakonczyc sukcesem:
    >> half = Ulamek(1, 2)
    >> print(half.licznik)
    1
    >> print(half.mianownik)
    2
    >> quarter = Ulamek(1, 4)
    >> print(quarter.licznik)
    1
    >> print(quarter.mianownik)
    4
    >> result = half + quarter  # 1/2 + 1/4
    >> print(result.licznik)
    6
    >> print(result.mianownik)
    8
    Zauwaz, ze nie chcemy w tym przypadku skracac ulamka do postaci 3/4. Algorytm zamienia 1/2 na 4/8 a 1/4 na 2/8
    (po prostu wymnaza liczby przez siebie).
"""


class Ulamek:
    def __init__( self, licznik, mianownik ):
        self.licznik = licznik
        self.mianownik = mianownik

    def __common_denominator( self, other ):
        max_m = max([self.mianownik, other.mianownik])
        common_denominator = 0
        for i in range(max_m, max_m ** max_m):
            if i % self.mianownik == 0 and i % other.mianownik == 0:
                common_denominator = int(i)
                break

        self.licznik = int((common_denominator / self.mianownik) * self.licznik)
        other.licznik = int((common_denominator / other.mianownik) * other.licznikss)

        return self.licznik, common_denominator, other.licznik, common_denominator

    def __add__( self, other ):
        self.licznik, self.mianownik, other.licznik, other.mianownik = self.__common_denominator(other)
        return Ulamek((self.licznik + other.licznik), self.mianownik)

    def __sub__( self, other ):
        self.licznik, self.mianownik, other.licznik, other.mianownik = self.__common_denominator(other)
        return Ulamek((self.licznik - other.licznik), self.mianownik)

    def __mul__( self, other ):
        return Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)

    def __truediv__( self, other ):
        return Ulamek(self.licznik * other.mianownik, other.licznik * self.mianownik)

    def __repr__( self ):
        return f"licznik -> {self.licznik} ," \
               f"mianownik -> {self.mianownik}"


def check_ulamek():
    ulamek_2 = Ulamek(1, 2)
    ulamek_1 = Ulamek(2, 3)

    res_add = ulamek_1 + ulamek_2
    res_sub = ulamek_1 - ulamek_2
    res_mul = ulamek_1 * ulamek_2
    res_truediv = ulamek_1 / ulamek_2

    print("add", res_add)
    print("sub", res_sub)
    print("mul", res_mul)
    print("truediv", res_truediv)


if __name__ == "__main__":
    check_ulamek()  # ok
