import unittest
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from colorama import Fore

class TestMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n[Exercice 08] trace')
        print('----------------------------------------------------------------------')
        print('\n[matrix]')
        print('----------------------------------------------------------------------')
    def setUp(self):
        print(Fore.LIGHTCYAN_EX, self.shortDescription(), Fore.RESET)
    
    def test_trace(self):
        u = Matrix([[1., 0.], [0., 1.]])
        self.assertEqual(u.trace(), 2.0)

        u = Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]])
        self.assertEqual(u.trace(), 9.0)
    
        u = Matrix([[-2., -8., 4.], [1., -23., 4.], [0., 6., 4.]])
        self.assertEqual(u.trace(), -21.0)
