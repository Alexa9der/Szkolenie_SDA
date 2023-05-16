"""
     Napisz program, który pobiera od użytkownika liczbę N,
     następnie tworzy słownik z kluczami od 1 do N z wartościami,
     które są kwadratami kluczy.
"""
n = int(input("Podaj liczbę N :\n"))

square_dictionary = {i: i ** 2 for i in range(1, n)}
print(square_dictionary)
