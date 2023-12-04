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
        print('\n[Exercice 00] add, substract and scale')
        print('----------------------------------------------------------------------')
        print('\n[matrix]')
        print('----------------------------------------------------------------------')
    def setUp(self):
         print(Fore.LIGHTCYAN_EX, self.shortDescription(), Fore.RESET)
    def test_row_echelon(self):
        u = Matrix([[1., 0., 0], [0., 1, 0], [0., 0., 1]])
        res = u.row_echelon()
        print(res.__str__(), type(res))
        
        u = Matrix([[1., 2.], [3., 4.]])
        res = u.row_echelon()
        print(res.__str__(), type(res))

        u = Matrix([[1., 2.], [2., 4.]])
        res = u.row_echelon()
        print(res.__str__(), type(res))

        u4 = Matrix([[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]])
        res = u4.row_echelon()
        print(res.__str__(), type(res))
        # testing find_pivot
        # u4 = Matrix([[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]])
        # res = u4.row_echelon()
        # print(res.__str__(), type(res))

        # u4 = Matrix([[1., 0.625, -0.25, 0.5, 3.5], [0., 0., 21., 2., -18.], [0., 0., 3., 0., -11.]])
        # res = u4.row_echelon()

