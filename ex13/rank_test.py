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
    def test_rank(self):
        u = Matrix([[1., 0., 0], [0., 1, 0], [0., 0., 1]])
        rank =  u.rank()
        self.assertEqual(rank, 3)
        print(f'Matrix:\n{u.__str__()}\rrank = {rank}\n')

        u = Matrix([[1., 2., 0., 0.], [2., 4., 0., 0.], [-1., 2., 1., 1.]])
        rank =  u.rank()
        self.assertEqual(rank, 2)
        print(f'Matrix:\n{u.__str__()}\rrank = {rank}\n')
        
        u = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.], [21., 18., 7.]])
        rank =  u.rank()
        self.assertEqual(rank, 3)
        print(f'Matrix:\n{u.__str__()}\rrank = {rank}\n')
