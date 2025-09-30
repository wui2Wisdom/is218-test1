"""Tests for the calculator module."""
from calculator import Calculator


class TestCalculator:
    """Test class for Calculator."""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(10, 15) == 25

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        calc = Calculator()
        assert calc.add(-2, -3) == -5
        assert calc.add(-10, 5) == -5

    def test_add_zero(self):
        """Test addition with zero."""
        calc = Calculator()
        assert calc.add(0, 5) == 5
        assert calc.add(5, 0) == 5
        assert calc.add(0, 0) == 0

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(10, 4) == 6

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        calc = Calculator()
        assert calc.subtract(3, 5) == -2
        assert calc.subtract(0, 10) == -10

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        calc = Calculator()
        assert calc.subtract(5, 0) == 5
        assert calc.subtract(0, 5) == -5

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        calc = Calculator()
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(4, 5) == 20

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        calc = Calculator()
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(-2, -3) == 6

    def test_multiply_zero(self):
        """Test multiplication with zero."""
        calc = Calculator()
        assert calc.multiply(5, 0) == 0
        assert calc.multiply(0, 5) == 0