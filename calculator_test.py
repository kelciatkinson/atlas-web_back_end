import unittest
from parameterized import parameterized
from calculator import Calculator
from unittest.mock import patch

class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
 
    @parameterized.expand([
            (10,2,5),
            (4,4,1),
            (4,2,2)
    ])
    def test_divide_positive_numbers(self, param1, param2, expectedResult) -> None:
        """test checks for postitive nums"""
        self.assertEqual(self.calculator.divide(param1, param2), expectedResult)
 
    @parameterized.expand([
            (0,5,0),
            (0,4,0)
    ])
    def test_divide_zero_by_positive_number(self, par1, par2, expected ) -> None:
        actual = self.calculator.divide(par1, par2)
        self.assertEqual(actual, expected)
 
    def test_divide_negative_by_positive_number(self) -> None:
        self.assertEqual(self.calculator.divide(-10, 2), -5)
 
    def test_divide_by_zero_should_raise_error(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    def test_add(self) -> None:
        actual = self.calculator.add(5,5)
        expected = 10
        self.assertEqual(actual, expected)

    @patch.object(Calculator, 'add', return_value=10)  # Mocking 'add' method
    def test_mocked_add(self, mock_add):
        result = self.calculator.add(2, 3)  # This will call 'add' but return the mocked value
        self.assertEqual(result, 10)  # Return value is mocked to be 10
        
    def tearDown(self) -> None:
        del self.calculator
