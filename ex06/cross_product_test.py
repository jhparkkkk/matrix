import unittest
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from colorama import Fore
from ex06.cross_product import cross_product


class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n[Exercice 06] Cross product")
        print("\n[vector]")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.YELLOW)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_cross_product_invalid_size(self):
        """test cross product with invalid size"""
        u = Vector([1.0])
        v = Vector([1.0, 1.0, 1.0])
        with self.assertRaises(ValueError) as cm:
            cross_product(u, v)
        self.assertEqual(str(cm.exception), "vector must contains 3 values")
        print(f"u = {u.__str__()}\nv = {v.__str__()}\n{cm.exception}\n")
        u = Vector([1.0, 1.0, 1.0])
        v = Vector([1.0])
        with self.assertRaises(ValueError) as cm:
            cross_product(u, v)
        self.assertEqual(str(cm.exception), "vector must contains 3 values")
        print(f"u = {u.__str__()}\nv = {v.__str__()}\n{cm.exception}")

    def test_cross_product(self):
        """test cross product"""
        u = Vector([0.0, 0.0, 1.0])
        v = Vector([1.0, 0.0, 0.0])
        cross = cross_product(u, v)
        self.assertEqual(cross.data, [0.0, 1.0, 0.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u × v = {cross.data}\n")
        u = Vector([1.0, 2.0, 3.0])
        v = Vector([4.0, 5.0, 6.0])
        cross = cross_product(u, v)
        self.assertEqual(cross.data, [-3.0, 6.0, -3.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u × v = {cross.data}\n")
        u = Vector([4.0, 2.0, -3.0])
        v = Vector([-2.0, -5.0, 16.0])
        cross = cross_product(u, v)
        self.assertEqual(cross.data, [17.0, -58.0, -16.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u × v = {cross.data}\n")
        u = Vector([3.0, 0.0, 2.0])
        v = Vector([-1.0, 4.0, 2.0])
        cross = cross_product(u, v)
        self.assertEqual(cross.data, [-8.0, -8.0, 12.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u × v = {cross.data}\n")
