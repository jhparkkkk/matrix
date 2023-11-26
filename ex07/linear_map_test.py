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
        print('\n[Exercice 07] linear map and matrix multiplication')
        print('----------------------------------------------------------------------')
        print('\n[matrix]')
        print('----------------------------------------------------------------------')
    def setUp(self):
         print(Fore.LIGHTCYAN_EX, self.shortDescription(), Fore.RESET)
    def test_linear_map(self):
        u = Matrix([[1., 0.], [0., 1.]])
        v = Vector([4., 2.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}\n")
        self.assertEqual(u.mul_vec(v).data, [4., 2.])
        print(f"uv = {u.mul_vec(v).data.__str__()}\n")

        u = Matrix([[2., 0.], [0., 2.]])
        v = Vector([4., 2.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}\n")
        self.assertEqual(u.mul_vec(v).data, [8., 4.])
        print(f"uv = {u.mul_vec(v).data.__str__()}\n")

        u = Matrix([[2., -2.], [-2., 2.]])
        v = Vector([4., 2.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}\n")
        self.assertEqual(u.mul_vec(v).data, [4., -4.])
        print(f"uv = {u.mul_vec(v).data.__str__()}\n")

    def test_matrix_multiplication(self):
        u = Matrix([[1., 0.], [0., 1.]])
        v = Matrix([[1., 0.], [0., 1.]])
        self.assertEqual(u.mul_mat(v).data, [[1., 0.], [0., 1.]])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}\n")
        print(f"uv = {u.mul_mat(v).data.__str__()}\n")

        u = Matrix([[1., 0.], [0., 1.]])
        v = Matrix([[2., 1.], [4., 2.]])
        self.assertEqual(u.mul_mat(v).data, [[2., 1.], [4., 2.]])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}\n")
        print(f"uv = {u.mul_mat(v).data.__str__()}\n")

        u = Matrix([[3., -5.], [6., 8.]])
        v = Matrix([[2., 1.], [4., 2.]])
        self.assertEqual(u.mul_mat(v).data, [[-14., -7.], [44., 22.]])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}\n")
        print(f"uv = {u.mul_mat(v).data.__str__()}\n")