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
        print('\n[vector]')
        print('----------------------------------------------------------------------')
    def setUp(self):
        print(Fore.YELLOW, self.shortDescription(), Fore.RESET)
    def test_cross_product_invalid_size(self):
        u = Vector([1.])
        v = Vector([1., 1., 1.])
        with self.assertRaises(ValueError) as cm:
            cross_product(u, v)
        self.assertEqual(str(cm.exception), 'vector must contains 3 values')
        u = Vector([1., 1., 1.])
        v = Vector([1.])
        with self.assertRaises(ValueError) as cm:
            cross_product(u, v)
        self.assertEqual(str(cm.exception), 'vector must contains 3 values')

    def test_cross_product(self):
        u = Vector([0., 0., 1.])
        v = Vector([1., 0., 0.])
        cross = cross_product(u, v)
        self.assertEqual(cross.data, [0., 1., 0.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u × v = {cross.data}\n")
        u = Vector([1., 2., 3.])
        v = Vector([4., 5., 6.])
        cross = cross_product(u, v)
        self.assertEqual(cross.data, [-3., 6., -3.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u × v = {cross.data}\n")
        u = Vector([4., 2., -3.])
        v = Vector([-2., -5., 16.])
        cross = cross_product(u, v)
        self.assertEqual(cross.data, [17., -58., -16.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u × v = {cross.data}\n")
        u = Vector([3., 0., 2.])
        v = Vector([-1., 4., 2.])
        cross = cross_product(u, v)
        self.assertEqual(cross.data, [-8., -8., 12.])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u × v = {cross.data}\n")