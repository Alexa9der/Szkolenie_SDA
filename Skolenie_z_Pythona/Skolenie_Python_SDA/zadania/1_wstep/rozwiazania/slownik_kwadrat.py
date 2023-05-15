"""
     Napisz program, który pobiera od użytkownika liczbę N,
     następnie tworzy słownik z kluczami od 1 do N z wartościami,
     które są kwadratami kluczy.
"""

n = int(input('Specify a number: '))
dictionary = {}

for i in range(1, n+1):
    dictionary[i] = i ** 2

for key, value in dictionary.items():
    print(f'The square of {key} is {value}.')
