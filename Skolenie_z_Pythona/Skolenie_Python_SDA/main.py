# Zadanie 1
'''Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową'''
def numbers_translator(num : str) -> str:

    num = map(int, list(num))
    text_numbers = {1:"jeden", 2:"dwa",3:"trzy", 4:"cztery",5:"Pięć", 6: "Sześć", 7:"siedem", 8: "osiem", 9:"dziewięć" }
    result = [ v for k, v in text_numbers.items() if k in num ]
    return result

# print( *numbers_translator(input()) )

# Zadanie 2

""" Stwórz funkcję przyjmującą listę liczb całkowitych, a zwracającą informację, na której pozycji znajduje się najmniejsza liczba.
Nie korzystaj z wbudowanych funkcji.np. dla listy [42, 13, 56, 7, 12, 3, 85] funkcja powinna zwrócić 5, ponieważ pod tym 
indeksem w tej liście znajduje się element najmniejszy."""
def min_num(numbers: list) -> int:

    index = 0
    num = numbers[-1]
    for i, v in enumerate(numbers):
        if num > v:
            num = v
            index = i
    return index

l = [11,2,3,4,1,5]
# print("index min nambers ->", min_num(l))


# Zadanie 3
"""Stwórz funkcję, która sprawdzi, czy liczba podana w argumencie jest pierwsza.
Funkcja powinna przyjmować wartość numeryczną, a zwracać powinna wartość logiczną True/False.
Np.Dla 11 funkcja zwróci True, natomiast dla 12 -> False."""

def foo (nums: int) -> bool:
    result = True
    for i in range(2, nums):
        if nums % i == 0 : result = False
    return result

# print(foo(1))

# Zadanie 4
"""Stwórz funkcję, która sprawdzi, czy podany jako argument napis jest palindromem (tj. czytany od przodu i wspak jest 
dokładnie taki sam, np. „kajak”, „Madam”)."""
def palindrom (slowo: str)->bool:
    slowo_odw = slowo[::-1]
    result = False
    if slowo_odw == slowo: result = True
    return result

# print( palindrom("13131"))

# Zadanie 5
""" Stwórz funkcję, która obliczy liczbę małych i wielkich liter w ciągu.
np. dla : “The quick Brown Fox” oczekiwany wynik :LIczba wielkich liter : 3, liczba małych liter : 13
Podpowiedź: wykorzystaj pętlę, instrukcję warunkową i odpowiednie metody dla stringa."""
def number_of_characters(text: str) -> tuple:
    """return 0 -> littl , 1 -> big"""
    little = 0
    big = 0
    for i in text:
        if i == i.lower() and i != " ": little += 1
        elif i != i.lower() and i != " ": big += 1
    return little, big

littl , big = number_of_characters("IdZe aaaa SpaC")

# print(f"Liczba wielkich liter : {big} ", f"liczba małych liter {littl}")

# Zadanie 6
"""Napisz funkcję, która przyjmuje dwa stringi i sprawdza, czy są swoimi anagramami.Na przykład:

„army” i „Mary”, „dzielenia” i „niedziela”, „Quid est veritas?” i „Vir est qui adest”, „Jim Morrison” i „Mr Mojo Risin”, „Tom Marvolo Riddle” 
i „I am Lord Voldemort” """
def anagram(text_1: str, text_2: str) -> str:

    def clear_text(text):
        text = text.lower()
        ignor_symbols = [" ", "?", ",", "!", '\"', "\'", "."]

        for i in ignor_symbols:
            if i in text: text = text.replace(i, "")

        return list(text)

    def counter_text(text):
        litery = dict()
        for i in text:
            count = 0
            for j in text:
                if i == j : count +=1
                litery[i] = count
        return litery
    text_1 = clear_text(text_1)
    text_2 = clear_text(text_2)

    text_1 = counter_text(text_1)
    text_2 = counter_text(text_2)

    result ="Są anagramami" # True
    for k, v in text_1.items():
        if k in text_2:
            if text_2[k] != v:
                result ="Nie są anagramami" #False
                break
        else:
            result = "Nie są anagramami" # False
            break

    return result

# print( anagram("Andri.!?", "Andri "), sep="\n" )


# Zadanie 7
'''Napisz funkcję, która zwróci 5 najczęstszych słów z dzieła Mickiewicza.
https://pastebin.com/raw/aAHeW5Pt (przekopiuj i zapisz do pliku tekstowego to, co znajdziesz pod tym linkiem).
Podpowiedź: skorzystaj z funkcji open(), metody split(), słownika oraz pętli.'''

with open("Dzialo_Mickiewicza.txt", encoding="utf8") as f:
    text = f.read().lower().split()

    count_words = dict()
    for i in text:
        count_words[i] = text.count(i)

# print(*sorted(count_words.items(), key= lambda x: x[1], reverse= True)[:5])


# Zadanie 8
'''Stwórz klasę Prostokąt, której atrybutami będą wysokość i szerokość figury.
Zaimplementuj metody do mierzenia obwodu i pola prostokąta.
Następnie stwórz klasę Kwadrat pamiętając, że każdy kwadrat jest prostokątem, ale nie każdy prostokąt jest kwadratem.'''
class Rectangle(): # Prostokąt
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter_rectangle(self): # obwod
        return 2* self.height + 2 * self.width

    def area_rectangle(self): # pole
        return self.height * self.width

rectangle = Rectangle(4, 2)
# print(rectangle.perimeter_rectangle())
# print(rectangle.area_rectangle())

class Square(Rectangle):
    def __init__(self, height, width):
        super().__init__(height=height, width=width)


square = Square(1, 1)

# print(square.height)
# print(square.width)



# Zadanie 9
"""Stwórz dekorator o nazwie debug, który podczas wywoływania funkcji będzie wyświetlał informacje o jej nazwie, przekazanych parametrach oraz zwracanym wyniku."""

def debag(func):
    def wraper(*arg, **kwargs):
        print(func.__name__+"(" , *arg, kwargs, ")", "zwróciła", func(*arg, *kwargs.values()) )

        return func(*arg, *kwargs.values())
    return wraper



# Zadanie 10
# Napisz program, który zwróci wartość bezwzględną liczby pobranej od
# użytkownika. Program powinien pytać o tę liczbę tak długo, aż nie zostanie
# ona poprawnie podana.

# Pamiętaj, że użytkownik nie zawsze wpisze wartość numeryczną, może
# też wpisać np. “kalafior”. Sprawdź, co wtedy się stanie i pamiętaj o obsłudze
# wyjątków

def input_nums() -> int:
    try:
        num = int(input())
        return num  # ?????
    except ValueError as error:
        print("Submit a number without any letters or symbols !!!!" )
        return input_nums()

# print(input_nums())












if __name__ == '__main__':
    ...


