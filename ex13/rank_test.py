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
        print("\n[Exercice 13] Rank")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.LIGHTCYAN_EX)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_rank(self):
        """test rank"""
        u = Matrix([[1.0, 0.0, 0], [0.0, 1, 0], [0.0, 0.0, 1]])
        rank = u.rank()
        self.assertEqual(rank, 3)
        print(f"Matrix:\n{u.__str__()}\rrank = {rank}\n")

        u = Matrix([[1.0, 2.0, 0.0, 0.0], [2.0, 4.0, 0.0, 0.0], [-1.0, 2.0, 1.0, 1.0]])
        rank = u.rank()
        self.assertEqual(rank, 2)
        print(f"Matrix:\n{u.__str__()}\rrank = {rank}\n")

        u = Matrix(
            [[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0], [21.0, 18.0, 7.0]]
        )
        rank = u.rank()
        self.assertEqual(rank, 3)
        print(f"Matrix:\n{u.__str__()}\rrank = {rank}\n")
