import math
import unittest
import sys
from Retirement_Implemented_Code import *
from types import *


# Implemented by Jeffry Herzog
class TakePercentage(unittest.TestCase):

    def test_percentage_1(self):
        self.assertEqual(take_percentage(100, 0.25), 25)
    def test_percentage_2(self):
        self.assertEqual(take_percentage(-50, 0.10), -5)


if __name__ == '__main__':
    unittest.main(exit=False)

