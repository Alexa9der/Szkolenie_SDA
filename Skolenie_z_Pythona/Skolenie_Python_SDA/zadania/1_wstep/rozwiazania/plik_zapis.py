"""
    Stwórz pusty plik tekstowy.
    Napisz program, który pobiera od użytkownika listę słów i zapisuje je w pliku.
"""

with open('file', 'w') as f:
    sentence = input('To save: ')
    f.write(sentence)
