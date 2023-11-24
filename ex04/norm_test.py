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
    def test_norm_1(self):
        """test manhattan norm
        """
        u = Vector([0., 0., 0.])
        self.assertEqual(u.norm_1(), 0.0)
        u = Vector([1., 2., 3.])
        self.assertEqual(u.norm_1(), 6.0)
        u = Vector([-1., -2.])
        self.assertEqual(u.norm_1(), 3.0)
        u = Vector([-1,-2,3,4,5])
        self.assertEqual(u.norm_1(), 15.0)
    def test_norm(self):
        """test euclidian norm
        """
        u = Vector([0., 0., 0.])
        self.assertEqual(u.norm(), 0.0)
        u = Vector([1., 2., 3.])
        self.assertEqual(u.norm(), 3.7416573867739413)
        u = Vector([-1., -2.])
        self.assertEqual(u.norm(), 2.23606797749979)

    def test_norm_inf(self):
        """test infinity norm
        """
        u = Vector([0., 0., 0.])
        self.assertEqual(u.norm_inf(), 0.0)

        u = Vector([1., 2., 3.])
        self.assertEqual(u.norm_inf(), 3.0)

        u = Vector([-1., -2.])
        self.assertEqual(u.norm_inf(), 2.0)


