import unittest
from io import StringIO
import sys
from unittest.mock import patch
import calculator

class TestCalculator(unittest.TestCase):
    def test_duplicate_welcome_message(self):
        """Тест проверяет, что приветствие выводится только один раз"""
        with patch('builtins.input', side_effect=['5']):
            captured_output = StringIO()
            sys.stdout = captured_output
            calculator.main()
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()
            welcome_count = output.count("Добро пожаловать в калькулятор!")
            self.assertEqual(welcome_count, 1, f"Приветствие выводится {welcome_count} раз, ожидается 1")

if __name__ == '__main__':
    unittest.main()
