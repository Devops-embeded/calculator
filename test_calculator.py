"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.Calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.Calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.Calculator.multiply(10, 10)
