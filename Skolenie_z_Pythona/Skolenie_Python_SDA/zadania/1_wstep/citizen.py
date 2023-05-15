"""
    Napisz klasę Citizen, która implementuje metodę __init__, przyjmującą dwa argumenty: first name i last name.
    Stwórz obiekt tej klasy, a następnie wyświetl imię i nazwisko obywatela.

    Dodaj metodę klasową set_nationality do klasy Citizen (a wraz z nią pole klasowe nationality
    o wybranej wartości domyślnej).
    Wywołaj tę metodę. Stwórz drugi obiekt klasy i zobacz, jaką wartość będzie miało pole nationality w obu obiektach.

    Dodatkowo możesz spróbować dodać atrybut klasowy total_number_of_citizens będący liczbą.
    Zwiększaj ją za każdym razem, kiedy tworzony będzie nowy obywatel.
"""


class Citizen:
    nationality = "Polish"
    total_number_of_citizens = 10

    def __init__( self, first_name, last_name, total_number_of_citizens=None ):
        self.first_name = first_name
        self.last_name = last_name
        Citizen.total_number_of_citizens += 1

    def __str__( self ):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def set_nationality( self, nationality ):
        self.nationality = nationality


vik_kov = Citizen("Viktoria", "Koval")
print(vik_kov.first_name, vik_kov.last_name)
print("\n")

mik_kov = Citizen("Mikolaj", "Koval")
print(mik_kov.first_name, mik_kov.last_name)
print("\n")

Citizen.nationality = "USA"
print(mik_kov.nationality)
print(vik_kov.nationality)