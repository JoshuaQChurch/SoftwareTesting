import math
import unittest
import sys
from types import *

def subtract_x_values(x_point1, x_point2):  # subtract X values
    return x_point2 - x_point1

def subtract_y_values(y_point1, y_point2):  # subtract Y Values
    return y_point2 - y_point1

class DistanceTest(unittest.TestCase):
    def test_xsubtract(self):
        result = subtract_x_values(2, 4)
        self.assertEqual(result, 2)
        
    def test_xsubtractneg(self):
        result = subtract_x_values(-1, -1)
        self.assertEqual(result, 0)

    def test_xsubtractneg2(self):
        result = subtract_x_values(1, -1)
        self.assertEqual(result, -2)
        
    def test_ysubtract(self):
        result = subtract_y_values(2, 4)
        self.assertEqual(result, 2)

    def test_ysubtractneg(self):
        result = subtract_y_values(-1, -1)
        self.assertEqual(result, 0)

    def test_ysubtractneg2(self):
        result = subtract_y_values(1, -1)
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main(exit=False)
