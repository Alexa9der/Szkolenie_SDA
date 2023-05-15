"""
    Napisz program, który wczytuje plik tekstowy,
    a następnie wypisuje go z ponumerowanymi liniami.
"""

PATH = ''  # sciezka do pliku tekstowego

if __name__ == '__main__':
    with open(PATH, 'r') as f:
        for index, line in enumerate(f.readlines(), 1):
            print(f'{index}. {line.strip()}')