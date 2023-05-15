"""
    Napisz program, który prosi użytkownika o podanie roku,
    a następnie sprawdza, czy dany rok jest przestępny.

    Rok jest przestępny, kiedy dzieli się przez 400 lub kiedy dzieli się
    przez 4, ale jednocześnie nie dzieli się przez 100.
"""

def is_leap_year(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    return leap

if __name__ == '__main__':
    year = int(input('Which year? '))
    print(f'{year} is leap: {is_leap_year(year)}')
