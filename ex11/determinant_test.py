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
        print("\n[Exercice 11] Determinant")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.LIGHTCYAN_EX)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_determinant(self):
        u = Matrix([[1.0, -1.0], [-1.0, 1.0]])
        determinant = u.determinant()
        self.assertEqual(determinant, 0.0)
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")

        u = Matrix([[3.0, 8.0], [4.0, 6.0]])
        determinant = u.determinant()
        self.assertEqual(determinant, -14.0)
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")

        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        determinant = u.determinant()
        self.assertEqual(determinant, -2.0)
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")

        u = Matrix([[2.5, 20.0, 4.0], [5.0, 1.0, 4.0], [-4.0, 17.0, 1.0]])
        determinant = u.determinant()
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")

        u = Matrix([[4, 20.0, 4.0], [8.0, 1.0, 4.0], [28.0, 17.0, 1.0]])
        determinant = u.determinant()
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")

        u = Matrix([[4, 2.5, 4.0], [8.0, 5.0, 4.0], [28.0, -4.0, 1.0]])
        determinant = u.determinant()
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")

        u = Matrix([[4, 2.5, 20.0], [8.0, 5.0, 1.0], [28.0, -4.0, 17.0]])
        determinant = u.determinant()
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")
        u = Matrix([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        determinant = u.determinant()
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")

        u = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
        determinant = u.determinant()
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")

        u = Matrix(
            [
                [8.0, 5.0, -2.0, 4.0],
                [4.0, 2.5, 20.0, 4.0],
                [8.0, 5.0, 1.0, 4.0],
                [28.0, -4.0, 17.0, 1.0],
            ]
        )
        determinant = u.determinant()
        print(f"Matrix:\n{u.__str__()}\rDeterminant = {determinant}\n")
