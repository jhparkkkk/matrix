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
        print("\n[Exercice 07] linear map and matrix multiplication")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.LIGHTCYAN_EX)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_linear_map(self):
        """test matrix multiplied by a vector"""
        u = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v = Vector([4.0, 2.0])
        self.assertEqual(u.mul_vec(v).data, [4.0, 2.0])
        print(f"Matrix U\n{u.__str__()}\nVector v\n{v.__str__()}\n")
        print(f"U x v =\n{u.mul_vec(v).data.__str__()}\n")

        u = Matrix([[2.0, 0.0], [0.0, 2.0]])
        v = Vector([4.0, 2.0])
        self.assertEqual(u.mul_vec(v).data, [8.0, 4.0])
        print(f"Matrix U\n{u.__str__()}\nVector v\n{v.__str__()}\n")
        print(f"uv = {u.mul_vec(v).data.__str__()}\n")

        u = Matrix([[2.0, -2.0], [-2.0, 2.0]])
        v = Vector([4.0, 2.0])
        self.assertEqual(u.mul_vec(v).data, [4.0, -4.0])
        print(f"Matrix U\n{u.__str__()}\nVector v\n{v.__str__()}\n")
        print(f"uv = {u.mul_vec(v).data.__str__()}\n")

    def test_matrix_multiplication(self):
        """test matrix multiplied by a matrix"""
        u = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v = Matrix([[1.0, 0.0], [0.0, 1.0]])
        self.assertEqual(u.mul_mat(v).data, [[1.0, 0.0], [0.0, 1.0]])
        print(f"Matrix U\n{u.__str__()}\nMatrix V\n{v.__str__()}\n")
        print(f"U x V = {u.mul_mat(v).data.__str__()}\n")

        u = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v = Matrix([[2.0, 1.0], [4.0, 2.0]])
        self.assertEqual(u.mul_mat(v).data, [[2.0, 1.0], [4.0, 2.0]])
        print(f"Matrix U\n{u.__str__()}\nMatrix V\n{v.__str__()}\n")
        print(f"U x V = {u.mul_mat(v).data.__str__()}\n")

        u = Matrix([[3.0, -5.0], [6.0, 8.0]])
        v = Matrix([[2.0, 1.0], [4.0, 2.0]])
        self.assertEqual(u.mul_mat(v).data, [[-14.0, -7.0], [44.0, 22.0]])
        print(f"Matrix U\n{u.__str__()}\nMatrix V\n{v.__str__()}\n")
        print(f"U x V = {u.mul_mat(v).data.__str__()}\n")
