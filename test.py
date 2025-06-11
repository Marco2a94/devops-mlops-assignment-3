import unittest
from Calculator import Calculator
from Converter import Converter

#Test pour déclancher la pipeline lors du pull request
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.converter = Converter()

    def test_non_existent_method(self):
        with self.assertRaises(AttributeError):
            self.calculator.non_existent_method()
            
    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)
        
    def test_subtract(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)
        
    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)
        
    def test_divide(self):
        result = self.calculator.divide(6, 3)
        self.assertEqual(result, 2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

    def test_convert_valid(self):
        result = self.converter.convert(100, 'EUR', 'USD')
        self.assertAlmostEqual(result, 118.0, places=2)

    def test_convert_invalid_currency(self):
        with self.assertRaises(ValueError):
            self.converter.convert(100, 'EUR', 'XYZ')