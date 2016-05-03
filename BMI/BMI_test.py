import math
import unittest
import sys
from BMI import *
from types import *


class Squaretesting(unittest.TestCase):

    def test_square1(self):
        self.assertEqual(square(3), 9)

    def test_square2(self):
        self.assertEqual(square(-2), 4)

    def test_square3(self):
        self.assertEqual(square(0), 0)

    def test_square4(self):
        self.assertEqual(square(1), 1)

if __name__ == '__main__':
    unittest.main(exit=False)

