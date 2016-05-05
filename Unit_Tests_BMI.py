import math
import unittest
import sys
from def_BMI import *
from types import *

#done by Corey Henry

class Squaretesting(unittest.TestCase):

    def test_square1(self):
        self.assertEqual(square(3), 9)

    def test_square2(self):
        self.assertEqual(square(-2), 4)

    def test_square3(self):
        self.assertEqual(square(0), 0)

    def test_square4(self):
        self.assertEqual(square(1), 1)

#done by Corey Henry

class Feet_to_inches_testing(unittest.TestCase):
    def test_fti1(self):
        self.assertEqual(ft_to_in(1), 12)

    def test_fti2(self):
        self.assertEqual(ft_to_in(2), 24)

    def test_fti3(self):
        self.assertEqual(ft_to_in(4), 48)

    #Jon Williams

    def test_decimal_feet(self):
    	self.assertEqual(ft_to_in(1.5), 18)

    def test_negative_inputF2I(self):
        self.assertRaises(OutOfRangeError,ft_to_in, -1)

    def test_negative_inputI2M(self):
        self.assertRaises(OutOfRangeError,convert_inch_meters, -1)
        
    def test_negative_inputL2K(self):
        self.assertRaises(OutOfRangeError,convert_lb_kg, -1)

    

    
    
#done by Corey Henry

class Divide_testing(unittest.TestCase):
    def test_d1(self):
        self.assertEqual(divide(4 , 2), 2)

    def test_d2(self):
        self.assertEqual(divide(20 , 5), 4)

    def test_d3(self):
        self.assertEqual(divide(75 , 3), 25)
        
#Jon Williams

    def test_negative_inputDivde_1(self):
        self.assertRaises(OutOfRangeError,divide, -1, 0)

    def test_negative_inputDivde_2(self):
        self.assertRaises(OutOfRangeError,divide, 0, -1)

    def test_negative_inputDivde_3(self):
        self.assertRaises(OutOfRangeError,divide, -1, -1)

    def test_negative_inputDivde_4(self):
        self.assertRaises(DivideByZero,divide, 1, 0)


if __name__ == '__main__':
    unittest.main(exit=False)

