import math
import unittest
import sys
from def_Retirement import *
from types import *


# Implemented by Jeffry Herzog
class TakePercentage(unittest.TestCase):

    def test_percentage_1(self):
        self.assertEqual(take_percentage(100, 0.25), 25)

##    def test_percentage_2(self):
##        self.assertEqual(take_percentage(-50, 0.10), -5)

    def test_percentage_3(self):
        self.assertEqual(take_percentage(115, 0), 0)

    #Jon Williams
    def test_negative_input_1(self):
        self.assertRaises(OutOfRangeError,take_percentage, -1, .1)
        
    def test_negative_input_2(self):
        self.assertRaises(OutOfRangeError,take_percentage, 1, -.1)
        
    


# Implemented by Jeffry Herzog
class Double(unittest.TestCase):

    def test_double_1(self):
        self.assertEqual(double(2), 4)

##    def test_double_2(self):
##        self.assertEqual(double(-4.5), -9)

    def test_double_3(self):
        self.assertEqual(double(0), 0)

    #Jon Williams
    def test_negative_input_1(self):
        self.assertRaises(OutOfRangeError,double, -1)

    def test_negative_input_2(self):
        self.assertRaises(OutOfRangeError,aging, -1)

    def test_negative_input_for_goal(self):
        self.assertRaises(OutOfRangeError,retirement, 1, 100, .1, -1)

    def test_negative_input_for_age(self):
        self.assertRaises(OutOfRangeError,retirement, -1, 100, .1, -1)


if __name__ == '__main__':
    unittest.main(exit=False)
