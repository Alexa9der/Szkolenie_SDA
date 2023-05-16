"""
    Napisz program, który prosi użytkownika o podanie roku,
    a następnie sprawdza, czy dany rok jest przestępny.

    Rok jest przestępny, kiedy dzieli się przez 400 lub kiedy dzieli się
    przez 4, ale jednocześnie nie dzieli się przez 100.
"""

year = 1988  # int(input("Podaj rok"))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Rok jest przestępny")
else:
    print("Rok jest nie przestępny")