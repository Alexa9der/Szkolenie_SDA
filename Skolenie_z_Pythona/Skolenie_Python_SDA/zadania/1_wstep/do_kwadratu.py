"""
    Napisz program, który poprosi użytkownika o liczbę naturalną (N) i wypisze wszystkie liczby
    od 1 do N podniesione do kwadratu (pętla for).
"""
nums = int(input("Poprosie o liczbę naturalną: "))

print("\nWszystkie liczby od 1 do N podniesione do kwadratu to:")
for square_nums in range(1, nums + 1):
    print(square_nums ** 2, end=" ")
