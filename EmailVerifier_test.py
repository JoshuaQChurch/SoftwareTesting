import unittest
import sys
from EmailVerifier import *

# Written by Joshua Church
class Domain(unittest.TestCase):
    def test_domain_1(self):
        self.assertEqual("edu", verifyDomain("jqc10@dasi.msstate.edu"))

    def test_dot_symbol(self):
        self.assertFalse(verifyDotSymbol("jqc10@dasi..msstate.edu"))
if __name__ == '__main__':
    unittest.main(exit=False)
