"""
    Napisz program, który wczytuje plik tekstowy, a następnie wypisuje go z ponumerowanymi liniami.
"""

with open("plik.txt", encoding="utf8") as file:
    text = file.readlines()
    for i, v in enumerate(text):
        print(i, v)
