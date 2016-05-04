#Written by: Jonathan Pongetti (Jpp192)

import unittest
import sys
from types import *
from def_DistanceFormula import *

        
class SubtractTest(unittest.TestCase):
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

class SquareTest(unittest.TestCase):
    def test_square_xvalue(self):
        result = square_x_value(2)
        self.assertEqual(result, 4)

    def test_square_xvaule2(self):
        result = square_x_value(-2)
        self.assertEqual(result, 4)

    def test_square_xvaule3(self):
        result = square_x_value(0)
        self.assertEqual(result, 0)

    def test_square_yvalue(self):
        result = square_y_value(2)
        self.assertEqual(result, 4)

    def test_square_yvaule2(self):
        result = square_y_value(-2)
        self.assertEqual(result, 4)

    def test_square_yvaule3(self):
        result = square_y_value(0)
        self.assertEqual(result, 0)
class AddTest(unittest.TestCase):
    def test_addVal(self):
        result = add_value(4, 4)
        self.assertEqual(result, 8)

    def test_addVal2(self):
        result = add_value(0, 0)
        self.assertEqual(result, 0)

    def test_addVal3(self):
        result = add_value (-1, -2)
        self.assertEqual(result, -3)

class getDistanceTest(unittest.TestCase):
    def test_GetDist(self):
        result = get_distance(4)
        self.assertEqual(result, 2)

    def test_GetDist2(self):
        self.assertRaises(ValueError, get_distance, -4)

class DistFormTest(unittest.TestCase):
    def test_DistFormula(self):
        result = distance_formula(2, 4, 5, 8)
        self.assertEqual(result, 5)

    def test_DistFormula2(self):
        result = distance_formula(4, 4, 4, 4)
        self.assertEqual(result, 0)
        
    def test_DistFormula3(self):
        result = distance_formula(4, 7, -2, 5)
        self.assertEqual(result, math.sqrt(40))

    def test_DistFormula4(self):
        result = distance_formula(0, 0, 0, 0)
        self.assertEqual(result, 0)

    #Test by Jon Williams

    def test_distanceFormulaIn2ndQuadrant(self):
        result = distance_formula(-1, 0, -2, 0)
        self.assertEqual(result, 1)

    def test_distanceFormulaIn3rdQuadrant(self):
        result = distance_formula(-1, -1, -2, -1)
        self.assertEqual(result, 1)

    def test_distanceFormulaIn4thQuadrant(self):
        result = distance_formula(1, -1, 2, -1)
        self.assertEqual(result, 1)

    def test_distanceFormulaFrom2to3Quad(self):
        result = distance_formula(-1, 1, -1, -1)
        self.assertEqual(result, 2)
        
    def test_distanceFormulaFrom3to4Quad(self):
        result = distance_formula(-1, -1, 1, -1)
        self.assertEqual(result, 2)

    def test_distanceFormulaFrom4to1Quad(self):
        result = distance_formula(1, 1, -1, -1)
        self.assertAlmostEqual(result, 2.8284271)

    def test_distanceFormulaFrom1to3Quad(self):
        result = distance_formula(1, 1, -1, -1)
        self.assertAlmostEqual(result, 2.8284271)

    def test_distanceFormulaFrom2to4Quad(self):
        result = distance_formula(-1, 1, 1, -1)
        self.assertAlmostEqual(result, 2.8284271)


        
if __name__ == '__main__':
    unittest.main(exit=False)
