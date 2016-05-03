import math
import unittest
import sys
from QA4_Main.py import *
from types import *


class Squaretesting(unittest.TestCase):

    def test_square1(self):
        self.assertEqual(3,9)

    def test_square2(self):
        self.assertEqual(-2,4)

    def test_square3(self):
        self.assertEqual(0,0)

    def test_square4(self):
        self.assertEqual(1,1)
