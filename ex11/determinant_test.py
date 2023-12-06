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
        print('\n[Exercice 11] Determinant')
        print('----------------------------------------------------------------------')
        print('\n[matrix]')
        print('----------------------------------------------------------------------')
    def setUp(self):
         print(Fore.LIGHTCYAN_EX, self.shortDescription(), Fore.RESET)
    
    def test_determinant(self):
        u = Matrix([[1., -1.], [-1., 1.]])
        determinant = u.determinant()
        self.assertEqual(determinant, 0.0)
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')
        
        u = Matrix([[3., 8.], [4., 6.]])
        determinant = u.determinant()
        self.assertEqual(determinant, -14.0)
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')

        u = Matrix([[1., 2.], [3., 4.]])
        determinant = u.determinant()
        self.assertEqual(determinant, -2.0)
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')
        
        u = Matrix([[2.5, 20., 4.], [5., 1., 4.], [-4., 17., 1.]])
        determinant = u.determinant()
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')

        u = Matrix([[4, 20., 4.], [8., 1., 4.], [28., 17., 1.]])
        determinant = u.determinant()
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')
        
        u = Matrix([[4, 2.5, 4.], [8., 5., 4.], [28., -4., 1.]])
        determinant = u.determinant()
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')
        
        u = Matrix([[4, 2.5, 20.], [8., 5., 1.], [28., -4., 17.]])
        determinant = u.determinant()
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')
        u = Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]])
        determinant = u.determinant()
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')
        
        u = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
        determinant = u.determinant()
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')

        u = Matrix([[ 8., 5., -2., 4.], [ 4., 2.5, 20., 4.], [ 8., 5., 1., 4.], [28., -4., 17., 1.],])
        determinant = u.determinant()
        print(f'Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n')
