"""
    Stwórz pusty plik tekstowy.
    Napisz program, który pobiera od użytkownika listę słów i zapisuje je w pliku.
"""

list_element = input("Podaj tekst do pliku: ")

with open("user_plik.txt", "w", encoding="utf8") as file:
    file.write(list_element)
