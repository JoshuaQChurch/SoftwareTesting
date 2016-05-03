import math
import unittest
import sys
from BMI import *
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
    

if __name__ == '__main__':
    unittest.main(exit=False)

