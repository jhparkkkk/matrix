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

    def test_add(self):
        """test add a vector
        """
        test = Vector()
        self.assertEqual(test.add(), "add")
        
    def test_subtract(self):
        """test substract a vector
        """
        test = Vector()

    def test_scale(self):
        """test multiply a vector by a scalar
        """
        test = Vector()

class TestMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n[Exercice 00] add, substract and scale')
        print('----------------------------------------------------------------------')
        print('\n[matrix]')
        print('----------------------------------------------------------------------')


    def setUp(self):
        print(self.shortDescription())

    def test_add(self):
        """test add a matrix
        """
        test = Matrix()
        self.assertEqual(test.add(), "add")
        
    def test_subtract(self):
        """test substract a matrix
        """
        test = Matrix()

    def test_scale(self):
        """test multiply a matrix by a scalar
        """
        test = Matrix()
