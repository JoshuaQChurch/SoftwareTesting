import unittest
import sys
from def_EmailVerifier import *

# Written by Joshua Church
class Domain(unittest.TestCase):
    def test_domain_1(self):
        self.assertNotEqual("edu", verifyDomain("jqc10@dasi.ms.edu"))

    def test_dot_symbol_1(self):
        self.assertFalse(verifyDotSymbol("jqc10@dasi..ms.edu"))

    def test_dot_symbol_2(self):
        self.assertTrue(verifyDotSymbol("jqc10@dasi.ms.edu"))

    def test_at_symbol_1(self):
        self.assertTrue(verifyAtSymbol("jjh258@ms.edu"))

    def test_at_symbol_2(self):
        self.assertFalse(verifyAtSymbol("jjh258ms.edu"))

    def test_verify_content_1(self):
        self.assertTrue(verifyContent("randEmail@joshua.co"))

    def test_verify_content_2(self):
        self.assertFalse(verifyContent("shouldFail.@.com"))

    def test_verify_content_3(self):
        self.assertFalse(verifyContent("WillFail@@test.com"))

    
if __name__ == '__main__':
    unittest.main(exit=False)
