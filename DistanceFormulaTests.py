#Written by: Jonathan Pongetti (Jpp192)

import math
import unittest
import sys
from types import *

def subtract_x_values(x_point1, x_point2):  # subtract X values
    return x_point2 - x_point1

def subtract_y_values(y_point1, y_point2):  # subtract Y Values
    return y_point2 - y_point1

def square_x_value(x_value):  # square X Values
    return x_value * x_value

def square_y_value(y_value):  # square Y Values
    return y_value * y_value

def add_value(x_squared, y_squared):  # add squared values together
    return x_squared + y_squared

def get_distance(total_before_squaring):  # get square root of distance
    return math.sqrt(total_before_squaring)

def distance_formula(x1_value, y1_value, x2_value, y2_value):  # aggregate functions to perform distance formula
    first_parenthesis = subtract_x_values(x1_value, x2_value)
    second_parenthesis = subtract_y_values(y1_value, y2_value)
    square_first_parenthesis = square_x_value(first_parenthesis)
    square_second_parenthesis = square_y_value(second_parenthesis)
    total_values = add_value(square_first_parenthesis, square_second_parenthesis)
    final_distance = get_distance(total_values)
    return final_distance
        
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
