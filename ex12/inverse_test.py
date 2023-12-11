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
    
    def test_inverse(self):
        u = Matrix([[1., 0., 0], [0., 1, 0], [0., 0., 1]])
        inverse = u.inverse()
        self.assertEqual(inverse, [[1., 0., 0], [0., 1, 0], [0., 0., 1]])
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {inverse}\n')

        u = Matrix([[2., 0., 0], [0., 2, 0], [0., 0., 2]])
        inverse = u.inverse()
        self.assertEqual(inverse, [[0.5, 0., 0], [0., 0.5, 0], [0., 0., 0.5]])
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {inverse}\n')

        u = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
        inverse = u.inverse()
        self.assertEqual(inverse, [[0.6494252873563219, 0.09770114942528736, -0.6551724137931034], [-0.7816091954022989, -0.12643678160919541, 0.9655172413793104], [0.14367816091954022, 0.07471264367816093, -0.20689655172413793]])
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {inverse}\n')



