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
        print('\n[vector]')
        print('----------------------------------------------------------------------')
    def setUp(self):
        print(Fore.YELLOW, self.shortDescription(), Fore.RESET)
    
    def test_dot_product(self):
        """test dot product
        """
        u = Vector([0., 0.])
        v = Vector([1., 1.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} ⋅ {v.__str__()}")
        self.assertEqual(u.dot(v), 0.0)
        print(f"u = {u.__str__()}\n")


        u = Vector([1., 1.])
        v = Vector([1., 1.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} ⋅ {v.__str__()}")
        self.assertEqual(u.dot(v), 2.0)
        print(f"u = {u.__str__()}\n")

        u = Vector([-1., 6.])
        v = Vector([3., 2.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} ⋅ {v.__str__()}")
        self.assertEqual(u.dot(v), 9.0)
        print(f"u = {u.__str__()}")

