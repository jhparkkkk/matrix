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
        print("\n[Exercice 04] Norm")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.YELLOW)
        print(self.shortDescription())
        print(Fore.RESET)
    def test_norm_1(self):
        """test manhattan norm
        """
        u = Vector([0., 0., 0.])
        norm = u.norm_1()
        self.assertEqual(norm, 0.0)
        print(f"u = {u.__str__()}\nmanhattan norm = {norm}\n")

        u = Vector([1., 2., 3.])
        norm = u.norm_1()
        self.assertEqual(norm, 6.0)
        print(f"u = {u.__str__()}\nmanhattan norm = {norm}\n")

        u = Vector([-1., -2.])
        norm = u.norm_1()
        self.assertEqual(norm, 3.0)
        print(f"u = {u.__str__()}\nmanhattan norm = {norm}\n")

        u = Vector([-1,-2,3,4,5])
        norm = u.norm_1()
        self.assertEqual(norm, 15.0)
        print(f"u = {u.__str__()}\nmanhattan norm = {norm}\n")
    def test_norm(self):
        """test euclidian norm
        """
        u = Vector([0., 0., 0.])
        norm = u.norm()
        self.assertEqual(norm, 0.0)
        print(f"u = {u.__str__()}\neuclidian norm = {norm}\n")

        u = Vector([1., 2., 3.])
        norm = u.norm()
        self.assertEqual(norm, 3.7416573867739413)
        print(f"u = {u.__str__()}\neuclidian norm = {norm}\n")

        u = Vector([-1., -2.])
        norm = u.norm()
        self.assertEqual(norm, 2.23606797749979)
        print(f"u = {u.__str__()}\neuclidian norm = {norm}\n")

    def test_norm_inf(self):
        """test infinity norm
        """
        u = Vector([0., 0., 0.])
        norm = u.norm_inf()
        self.assertEqual(norm, 0.0)
        print(f"u = {u.__str__()}\nsupremum norm = {norm}\n")

        u = Vector([1., 2., 3.])
        norm = u.norm_inf()
        self.assertEqual(norm, 3.0)
        print(f"u = {u.__str__()}\nsupremum norm = {norm}\n")

        u = Vector([-1., -2.])
        norm = u.norm_inf()
        self.assertEqual(norm, 2.0)
        print(f"u = {u.__str__()}\nsupremum norm = {norm}\n")


