import unittest
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from colorama import Fore
from ex02.linear_interpolation import lerp

class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n[vector]')
        print('----------------------------------------------------------------------')
    def setUp(self):
        print(Fore.YELLOW, self.shortDescription(), Fore.RESET)
    def test_scalar_field(self):
        """test scalar field K
        """
        self.assertEqual(lerp(0., 1., 0.), 0.)
        self.assertEqual(lerp(0., 1., 1.), 1.)
        self.assertEqual(lerp(0., 1., 0.5), 0.5)
        self.assertEqual(lerp(21., 42., 0.3), 27.3)

    def test_vector_field(self):
        result = lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3)
        self.assertEqual(result.data, [2.6, 1.3])
    def test_matrix_field(self):
        result = lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5)
        self.assertEqual(result.data, [[11., 5.5], [16.5, 22.]])
        print(f"res = {result.__str__()}")
    



class TestMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n[Exercice 00] add, substract and scale')
        print('----------------------------------------------------------------------')
        print('\n[matrix]')
        print('----------------------------------------------------------------------')
    def setUp(self):
         print(Fore.LIGHTCYAN_EX, self.shortDescription(), Fore.RESET)