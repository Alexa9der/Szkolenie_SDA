"""
    Poproś użytkownika o podanie elementów dla dwóch list.
    W tym celu użytkownik najpierw dodaje do pierwszej listy, aż wpisze zero.
    Następnie dodaje do drugiej listy, aż znów wpisze zero.
    Twoim zadaniem jest wyświetlić posortowaną różnicę symetryczną zbiorów utworzonych z tych dwóch list.
"""


# Różnica symetryczna zbiorów
#  A i B – zbiór, do którego należą elementy zbioru A nienależące do zbioru B oraz elementy należące do zbioru B, ale nienależące do zbioru A

def add_and_sorted_list( text: str ) -> str:
    sets = [input(text)]
    while sets[-1] != "0":
        sets.append(input())
    return sorted(sets)


def symmetrical_difference_of_sets( l1: list, l2: list ) -> list:
    diff_l1 = [i for i in l1 if i not in l2]
    diff_l2 = [i for i in l2 if i not in l1]
    return diff_l1 + diff_l2


set_a =  add_and_sorted_list("Podaj elementy do pierwszej listy dla tego aby zakończyć podaj zero:\n")
set_b =  add_and_sorted_list("Podaj elementy do drugej listy dla tego aby zakończyć podaj zero:\n")

print(
    f"To jest posortowaną różnicę symetryczną zbiorów utworzonych z tych dwóch list\n {symmetrical_difference_of_sets(set_a, set_b)}")
