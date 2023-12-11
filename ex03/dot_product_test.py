import unittest
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from colorama import Fore


class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n[Exercice 03] Dot product")
        print("\n[vector]")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.YELLOW)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_dot_product(self):
        """test dot product"""
        u = Vector([0.0, 0.0])
        v = Vector([1.0, 1.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"dot product = {u.__str__()} ⋅ {v.__str__()}")
        res = u.dot(v)
        self.assertEqual(res, 0.0)
        print(f"dot product = {res}")
        u = Vector([1.0, 1.0])
        v = Vector([1.0, 1.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"dot product = {u.__str__()} ⋅ {v.__str__()}")
        res = u.dot(v)
        self.assertEqual(res, 2.0)
        print(f"dot product = {res}")

        u = Vector([-1.0, 6.0])
        v = Vector([3.0, 2.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"dot product = {u.__str__()} ⋅ {v.__str__()}")
        res = u.dot(v)
        self.assertEqual(res, 9.0)
        print(f"dot product = {res}")
