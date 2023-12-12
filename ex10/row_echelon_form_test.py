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
    def setUp(self):
         print(Fore.LIGHTCYAN_EX, self.shortDescription(), Fore.RESET)
    def test_row_echelon(self):
        u = Matrix([[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])
        print(f'Matrix:\n{u.__str__()}')
        res = u.row_echelon()
        print(res.__str__())
        self.assertEqual(res.data, [[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])

        u = Matrix([[1., 0., 0.], [0., 0., 0.], [0., 0., 0.]])
        print(f'Matrix:\n{u.__str__()}')
        res = u.row_echelon()
        print(f'Reduced Matrix:\n{res.__str__()}')
        self.assertEqual(res.data, [[1., 0., 0.], [0., 0., 0.], [0., 0., 0.]])

        u = Matrix([[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]])
        print(f'Matrix:\n{u.__str__()}')
        res = u.row_echelon()
        print(f'Reduced Matrix:\n{res.__str__()}')
        self.assertEqual(res.data, [[1., 1., 1.], [0., 0., 0.], [0., 0., 0.]])
        
        u = Matrix([[1., 0., 0], [0., 1, 0], [0., 0., 1]])
        print(f'Matrix:\n{u.__str__()}')
        res = u.row_echelon()
        print(f'Reduced Matrix:\n{res.__str__()}')
        self.assertEqual(res.data, [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
        
        u = Matrix([[1., 2.], [3., 4.]])
        print(f'Matrix:\n{u.__str__()}')
        res = u.row_echelon()
        print(f'Reduced Matrix:\n{res.__str__()}')
        self.assertEqual(res.data, [[1., 0.], [0., 1.]])

        u = Matrix([[1., 2.], [2., 4.]])
        print(f'Matrix:\n{u.__str__()}')
        res = u.row_echelon()
        print(f'Reduced Matrix:\n{res.__str__()}')
        self.assertEqual(res.data, [[1., 2.], [0., 0.]])


        u4 = Matrix([[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]])
        print(f'Matrix:\n{u.__str__()}')
        res = u4.row_echelon()
        print(f'Reduced Matrix:\n{res.__str__()}')
        self.assertEqual(res.data, [[1.0, 0.625, 0.0, 0.0, -12.166666666666668], [0.0, 0.0, 1.0, 0.0, -3.6666666666666665], [-0.0, -0.0, -0.0, 1.0, 29.5]])
