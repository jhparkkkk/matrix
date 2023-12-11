import unittest
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from colorama import Fore
from ex05.cosine import angle_cos


class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n[Exercice 05] Cosine")
        print("\n[vector]")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.YELLOW)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_angle_cos_zero(self):
        """test cosine with vector filled with zeros"""
        u = Vector([0.0, 0.0])
        v = Vector([0.0, 0.0])
        with self.assertRaises(ValueError) as cm:
            angle_cos(u, v)
        self.assertEqual(str(cm.exception), "one of the vector is zero")
        print(f"u = {u.__str__()}\nv = {v.__str__()}\n{cm.exception}")

        u = Vector([0.0, 0.0])
        v = Vector([1.0, 1.0])
        with self.assertRaises(ValueError) as cm:
            angle_cos(u, v)
        self.assertEqual(str(cm.exception), "one of the vector is zero")
        print(f"u = {u.__str__()}\nv = {v.__str__()}\n{cm.exception}")

    def test_angle_cos_different_size(self):
        """test cosine with vectors of different size"""
        u = Vector([1.0, 2.0])
        v = Vector([3.0, 4.0, 5.0])
        with self.assertRaises(ValueError) as cm:
            angle_cos(u, v)
        self.assertEqual(str(cm.exception), "vectors are different size")
        print(f"u = {u.__str__()}\nv = {v.__str__()}\n{cm.exception}")

    def test_angle_cos(self):
        """test angle_cos"""
        u = Vector([3.0, 4.0])
        v = Vector([4.0, 3.0])
        self.assertEqual(angle_cos(u, v), 0.96)
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"cos α = {angle_cos(u, v)}\n")
        u = Vector([7.0, 1.0])
        v = Vector([5.0, 5.0])
        self.assertEqual(angle_cos(u, v), 0.8)
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"cos α = {angle_cos(u, v)}\n")
        u = Vector([1.0, 0.0])
        v = Vector([1.0, 0.0])
        self.assertEqual(angle_cos(u, v), 1.0)
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"cos α = {angle_cos(u, v)}\n")
        u = Vector([1.0, 0.0])
        v = Vector([0.0, 1.0])
        self.assertEqual(angle_cos(u, v), 0.0)
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"cos α = {angle_cos(u, v)}\n")
        u = Vector([-1.0, 1.0])
        v = Vector([1.0, -1.0])
        self.assertEqual(angle_cos(u, v), -1.0)
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"cos α = {angle_cos(u, v)}\n")
        u = Vector([2.0, 1.0])
        v = Vector([4.0, 2.0])
        self.assertEqual(angle_cos(u, v), 1.0)
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"cos α = {angle_cos(u, v)}\n")
        u = Vector([1.0, 2.0, 3])
        v = Vector([4.0, 5.0, 6])
        self.assertEqual(angle_cos(u, v), 0.974631846)
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"cos α = {angle_cos(u, v)}\n")
