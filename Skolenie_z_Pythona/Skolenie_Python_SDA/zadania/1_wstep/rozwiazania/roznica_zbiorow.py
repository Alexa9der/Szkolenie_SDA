"""
    Poproś użytkownika o podanie elementów dla dwóch list.
    W tym celu użytkownik najpierw dodaje do pierwszej listy, aż wpisze zero.
    Następnie dodaje do drugiej listy, aż znów wpisze zero.
    Twoim zadaniem jest wyświetlić posortowaną różnicę symetryczną zbiorów utworzonych z tych dwóch list.
"""

def create_list():
    mylist = []

    while True:
        number = int(input())
        if number == 0:
            break
        mylist.append(number)

    return mylist 

if __name__ == '__main__':
    print('Elements for the 1st list: ')
    list_1 = create_list()
    print('Elements for the 2nd list: ')
    list_2 = create_list()
    
    list_3 = list(set(list_1) ^ set(list_2))
    list_3.sort()
    print(list_3)
