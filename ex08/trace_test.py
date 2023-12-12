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
        print("\n[Exercice 08] trace")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.LIGHTCYAN_EX)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_trace_not_square(self):
        """test trace with matrix that is not square"""
        u = Matrix([[1.0, 0.0, 3.0], [0.0, 1.0, 2.0]])
        with self.assertRaises(TypeError) as cm:
            u.trace()
        self.assertEqual(str(cm.exception), "Matrix is not square")
        print(f"Matrix U\n{u.__str__()}\n{cm.exception}")

    def test_trace(self):
        """test trace"""
        u = Matrix([[1.0, 0.0], [0.0, 1.0]])
        self.assertEqual(u.trace(), 2.0)
        print(f"Matrix U\n{u.__str__()}\nTrace(U) = {u.trace()}\n")

        u = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
        self.assertEqual(u.trace(), 9.0)
        print(f"Matrix U\n{u.__str__()}\nTrace(U) = {u.trace()}\n")

        u = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]])
        self.assertEqual(u.trace(), -21.0)
        print(f"Matrix U\n{u.__str__()}\nTrace(U) = {u.trace()}\n")
