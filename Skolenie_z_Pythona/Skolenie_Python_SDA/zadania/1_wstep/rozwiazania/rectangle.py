"""
    Stwórz klasę o nazwie Rectangle.
    Klasa powinna mieć dwa pola dla boków oraz metodę area (property) do liczenia pola prostokąta.
"""

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    rect = Rectangle(11, 17)
    print(rect.area)
