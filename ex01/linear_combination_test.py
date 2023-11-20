import unittest
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix

class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n[vector]')
        print('----------------------------------------------------------------------')
    def setUp(self):
        print(self.shortDescription())
    def test_linear_combination(self):
        """test linear combination
        """


class TestMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n[Exercice 01] linear combination')
        print('----------------------------------------------------------------------')
        print('\n[matrix]')
        print('----------------------------------------------------------------------')
    def setUp(self):
        print(self.shortDescription())
    def test_linear_combination(self):
        """test linear combination
        """