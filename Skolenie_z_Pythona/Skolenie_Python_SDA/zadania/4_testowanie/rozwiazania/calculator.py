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
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(5, 2)

    def test_add(self):
        self.assertEqual(self.calc.add(), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(), 10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(), 2.5)

    def test_divide_zero(self):
        self.calc = Calculator(5, 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide()
