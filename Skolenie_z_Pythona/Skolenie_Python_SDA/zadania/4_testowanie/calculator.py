"""
    Stwórz klasę Calculator, w ktorej zaimplementujesz dzialania:
    - dodawanie,
    - odejmowanie,
    - mnozenie,
    - dzielenie.
    Napisz testy, które przetestuja wczesniej wymienione metody.
"""

import unittest


class Calculator:
    def __init__( self, x, y ):
        self.x = x
        self.y = y

    def add( self ):
        return self.x + self.y

    def subtraction( self ):
        return self.x - self.y

    def multiplikation( self ):
        return self.x * self.y

    def division( self ):
        if self.y != 0:
            return self.x / self.y
        else:
            raise ZeroDivisionError


class TestCalculator(unittest.TestCase):
    def test_class_calculator_add( self ):
        test = Calculator(3, 3)
        self.assertEqual(test.add(), 6)
        self.assertEqual(test.subtraction(), 0)
        self.assertEqual(test.division(), 1)
        self.assertEqual(test.multiplikation(), 9)

    def test_class_calculator_substraktion( self ):
        test = Calculator(5, 3)
        self.assertEqual(test.add(), 8)
        self.assertEqual(test.subtraction(), 2)
        self.assertEqual(test.division(), 1.6666666666666667)
        self.assertEqual(test.multiplikation(), 15)

    def test_class_calculator_division( self ):
        test = Calculator(10, 11)
        self.assertEqual(test.add(), 21)
        self.assertEqual(test.subtraction(), -1)
        self.assertEqual(test.division(), 0.9090909090909091)
        self.assertEqual(test.multiplikation(), 110)

    def test_class_calculator_multiplikation( self ):
        test = Calculator(30, 3)
        self.assertEqual(test.add(), 33)
        self.assertEqual(test.subtraction(), 27)
        self.assertEqual(test.division(), 10)
        self.assertEqual(test.multiplikation(), 90)


if __name__ == '__main__':
    unittest.main()
    # ok
