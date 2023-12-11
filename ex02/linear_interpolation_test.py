import unittest
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix
from colorama import Fore
from ex02.linear_interpolation import lerp


class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n[Exercice 02] Linear interpolation")
        print("\n[vector]")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.YELLOW)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_scalar_field(self):
        """test linear interpolation for scalar field K"""
        a = 0.0
        b = 1.0
        interpolation_factor = 0.0
        res = lerp(a, b, interpolation_factor)
        self.assertEqual(res, 0.0)
        print(
            f"a = {a}\nb = {b}\ninterpolation factor = {interpolation_factor}\nlerp = (1 - {interpolation_factor}) * {a} + {interpolation_factor} * {b} = {res}"
        )

        a = 0.0
        b = 1.0
        interpolation_factor = 1.0
        res = lerp(a, b, interpolation_factor)
        self.assertEqual(res, 1.0)
        print(
            f"\na = {a}\nb = {b}\ninterpolation factor = {interpolation_factor}\nlerp = (1 - {interpolation_factor}) * {a} + {interpolation_factor} * {b} = {res}"
        )

        a = 0.0
        b = 1.0
        interpolation_factor = 0.5
        res = lerp(a, b, interpolation_factor)
        self.assertEqual(res, 0.5)
        print(
            f"\na = {a}\nb = {b}\ninterpolation factor = {interpolation_factor}\nlerp = (1 - {interpolation_factor}) * {a} + {interpolation_factor} * {b} = {res}"
        )

        a = 21.0
        b = 42.0
        interpolation_factor = 0.3
        res = lerp(a, b, interpolation_factor)
        self.assertEqual(res, 27.3)
        print(
            f"\na = {a}\nb = {b}\ninterpolation factor = {interpolation_factor}\nlerp = (1 - {interpolation_factor}) * {a} + {interpolation_factor} * {b} = {res}"
        )

    def test_vector_field(self):
        """test linear interpolation for vector field V"""
        u = Vector([2.0, 1.0])
        v = Vector([4.0, 2.0])
        interpolation_factor = 0.3
        res = lerp(u, v, interpolation_factor)
        self.assertEqual(res.data, [2.6, 1.3])
        print(
            f"\nu = {u}\nv = {v}\ninterpolation factor = {interpolation_factor}\nlerp = (1 - {interpolation_factor}) * {u} + {interpolation_factor} * {v} = {res}"
        )

        u = Vector([2.0, 1.0])
        v = Vector([4.0, 2.0])
        interpolation_factor = 0
        res = lerp(u, v, interpolation_factor)
        self.assertEqual(res.data, [2.0, 1.0])
        print(
            f"\nu = {u}\nv = {v}\ninterpolation factor = {interpolation_factor}\nlerp = (1 - {interpolation_factor}) * {u} + {interpolation_factor} * {v} = {res}"
        )

        u = Vector([2.0, 1.0])
        v = Vector([4.0, 2.0])
        interpolation_factor = 1
        res = lerp(u, v, interpolation_factor)
        self.assertEqual(res.data, [4.0, 2.0])
        print(
            f"\nu = {u}\nv = {v}\ninterpolation factor = {interpolation_factor}\nlerp = (1 - {interpolation_factor}) * {u} + {interpolation_factor} * {v} = {res}"
        )

        u = Vector([2.0, 1.0])
        v = Vector([4.0, 2.0])
        interpolation_factor = 0.5
        res = lerp(u, v, interpolation_factor)
        self.assertEqual(res.data, [3.0, 1.5])
        print(
            f"\nu = {u}\nv = {v}\ninterpolation factor = {interpolation_factor}\nlerp = (1 - {interpolation_factor}) * {u} + {interpolation_factor} * {v} = {res}"
        )

    def test_matrix_field(self):
        """test linear interpolation for matrix field M"""
        u = Matrix([[2.0, 1.0], [3.0, 4.0]])
        v = Matrix([[20.0, 10.0], [30.0, 40.0]])
        interpolation_factor = 0.5
        res = lerp(u, v, interpolation_factor)
        self.assertEqual(res.data, [[11.0, 5.5], [16.5, 22.0]])
        print(
            f"\nu = {u}\nv = {v}\ninterpolation factor = {interpolation_factor}\nlerp = (1 - {interpolation_factor}) * {u} + {interpolation_factor} * {v} = {res}"
        )
