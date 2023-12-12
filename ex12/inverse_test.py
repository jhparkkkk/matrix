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
        print("\n[Exercice 12] Inverse")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.LIGHTCYAN_EX)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_inverse_singular(self):
        """test inverse with a singular matrix meaning det(U) = 0"""
        U = Matrix([[1.0, -1.0], [-1.0, 1.0]])
        with self.assertRaises(TypeError) as cm:
            inverse = U.inverse()
        self.assertEqual(
            str(cm.exception), "Cannot compute Inverse: matrix is singular"
        )
        print(f"Matrix:\n{U.__str__()}\rInverse = {cm.exception}\n")

    def test_inverse_not_square(self):
        """test inverse with a non square matrix"""
        U = Matrix([[1.0, -1.0], [-1.0, 1.0], [2.0, 2.0]])
        with self.assertRaises(TypeError) as cm:
            inverse = U.inverse()
        self.assertEqual(str(cm.exception), "Matrix is not square")
        print(f"Matrix:\n{U.__str__()}\rInverse = {cm.exception}\n")

    def test_inverse(self):
        """test inverse"""
        U = Matrix([[1.0, 0.0, 0], [0.0, 1, 0], [0.0, 0.0, 1]])
        inverse = U.inverse()
        self.assertEqual(inverse, [[1.0, 0.0, 0], [0.0, 1, 0], [0.0, 0.0, 1]])
        print(f"Matrix:\n{U.__str__()}\rInverse = {inverse}\n")

        U = Matrix([[2.0, 0.0, 0], [0.0, 2, 0], [0.0, 0.0, 2]])
        inverse = U.inverse()
        self.assertEqual(inverse, [[0.5, 0.0, 0], [0.0, 0.5, 0], [0.0, 0.0, 0.5]])
        print(f"Matrix:\n{U.__str__()}\rInverse = {inverse}\n")

        U = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
        inverse = U.inverse()
        self.assertEqual(
            inverse,
            [
                [0.6494252873563219, 0.09770114942528736, -0.6551724137931034],
                [-0.7816091954022989, -0.12643678160919541, 0.9655172413793104],
                [0.14367816091954022, 0.07471264367816093, -0.20689655172413793],
            ],
        )
        print(f"Matrix:\n{U.__str__()}\rInverse = {inverse}\n")
