import unittest
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from colorama import Fore

class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n[vector]')
        print('----------------------------------------------------------------------')

    def setUp(self):
        print(Fore.YELLOW, self.shortDescription(), Fore.RESET)
    
    def test_utils(self):
        """test utilitary functions
        - get_size()
        - __str__()
        - reshape() 
        """
        test = Vector([1.0, 1.0])
        self.assertEqual(test.__str__(), '[1.0, 1.0]')
        self.assertEqual(test.get_size(), 2)
        try:
            empty = Vector([])
        except ExceptionError as error:
            print(f"TypeError: {error}")
        
        test_reshape = Vector([1, 2, 3, 4, 5, 6])
        self.assertEqual(test_reshape.reshape(2, 3), [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        try:
            self.assertEqual(test_reshape.reshape(2, 2), [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        except ValueError as error:
            print(f"ValueError: {error}")

    def test_add(self):
        """test add a vector
        """
        u = Vector([2., 3.])
        v = Vector([5., 7.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} + {v.__str__()}")
        self.assertEqual(u.add(v), [7.0, 10.0])
        print(f"u = {u.__str__()}\n")

        u = Vector([2.])
        v = Vector([5., 7.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} + {v.__str__()}")
        try:
            self.assertEqual(u.add(v), [7.0, 10.0])
        except ValueError as error:
            print(f"ValueError: {error}")
        
    def test_subtract(self):
        """test substract a vector
        """
        u = Vector([2., 3.])
        v = Vector([5., 7.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} + {v.__str__()}")
        self.assertEqual(u.sub(v), [-3.0, -4.0])
        print(f"u = {u.__str__()}\n")

        u = Vector([2.])
        v = Vector([5., 7.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} + {v.__str__()}")
        try:
            self.assertEqual(u.sub(v), [-3.0, -4.0])
        except ValueError as error:
            print(f"ValueError: {error}")

    def test_scale(self):
        """test multiply a vector by a scalar
        """
        u = Vector([2., 3.])
        print(f"u = {u.__str__()} * 2")
        self.assertEqual(u.scl(2.), [4.0, 6.0])
        print(f"u = {u.__str__()}")

class TestMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n[Exercice 00] add, substract and scale')
        print('----------------------------------------------------------------------')
        print('\n[matrix]')
        print('----------------------------------------------------------------------')


    def setUp(self):
        print(self.shortDescription())

    def test_utils(self):
        """test utilitary functions
        - get_shape()
        - __str__()
        - reshape()
        - is_square() 
        """
#     def test_add(self):
#         """test add a matrix
#         """
#         test = Matrix()
#         self.assertEqual(test.add(), "add")
        
#     def test_subtract(self):
#         """test substract a matrix
#         """
#         test = Matrix()

#     def test_scale(self):
#         """test multiply a matrix by a scalar
#         """
#         test = Matrix()
