"""
    Napisz program, który wyświetla
    najmniejszy i największy element listy, a także ją odwróci.
"""

list_element = input("Podaj liste elementuw pszez spacle: ").strip().split(" ")

max_element = list_element[-1]
min_element = list_element[-1]
reversed_element = list_element[::-1]

for i in list_element:
    if i > max_element: element = i
    if i < min_element: min_element = i

print(f"najmniejszy element: {min_element}")
print(f"największy element: {max_element}")
print(f"odwrócione elementy: {reversed_element} ")
