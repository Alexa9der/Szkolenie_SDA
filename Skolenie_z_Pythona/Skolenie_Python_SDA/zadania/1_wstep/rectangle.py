"""
    Stwórz klasę o nazwie Rectangle.
    Klasa powinna mieć dwa pola dla boków oraz metodę area (property) do liczenia pola prostokąta.
"""


class Rectangle:
    def __init__( self, length, width):
        self.length = length
        self.width = width

    @property
    def area( self):
        return self.length * self.width


ractangle = Rectangle(10, 4)
print(ractangle.area)
