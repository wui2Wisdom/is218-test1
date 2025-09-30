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