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
        print('\n[Exercice 09] transpose')
        print('----------------------------------------------------------------------')
    def setUp(self):
        print(Fore.LIGHTCYAN_EX)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_transpose(self):
        """test transpose
        """
        mat = Matrix([[1., 2.], [3., 4.], [5., 6.]])
        transposed = mat.transpose()
        print(f"original matrix = \n{mat.__str__()}")

        print(f"transposed matrix = \n{transposed.__str__()}")