import unittest
import sys
from def_EmailVerifier import *

# Written by Joshua Church
class Domain(unittest.TestCase):
    def test_domain_1(self):
        self.assertEqual("edu", verifyDomain("jqc10@dasi.msstate.edu"))

    def test_dot_symbol(self):
        self.assertFalse(verifyDotSymbol("jqc10@dasi..msstate.edu"))

    def test_at_symbol_1(self):
        self.assertTrue(verifyAtSymbol("jjh258@msstate.edu"))

    def test_at_symbol_2
if __name__ == '__main__':
    unittest.main(exit=False)
