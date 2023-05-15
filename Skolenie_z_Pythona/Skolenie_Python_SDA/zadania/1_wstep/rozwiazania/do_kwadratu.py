"""
    Napisz program, który poprosi użytkownika o liczbę naturalną (N) i wypisze wszystkie liczby
    od 1 do N podniesione do kwadratu (pętla for).
"""

limit = int(input('Specify the limit: '))

for i in range(limit):
    print(i**2)
