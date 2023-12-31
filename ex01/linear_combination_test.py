from ex01.linear_combination import linear_combination
from colorama import Fore
from linear_algebra.matrix import Matrix
from linear_algebra.vector import Vector
import unittest
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n[Exercice 01] Linear combination")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.YELLOW)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_linear_combination(self):
        """test linear combination of vectors"""
        e1 = Vector([1.0, 0.0, 0.0])
        e2 = Vector([0.0, 1.0, 0.0])
        e3 = Vector([0.0, 0.0, 1.0])
        print(f"e1 = {e1.__str__()}")
        print(f"e2 = {e2.__str__()}")
        print(f"e3 = {e3.__str__()}")
        print("coef = [10.0, -2.0, 0.5]")
        res = linear_combination([e1, e2, e3], [10.0, -2.0, 0.5])
        self.assertEqual(res.data, [10.0, -2.0, 0.5])
        print(f"result = {res.__str__()}\n")

        v1 = Vector([1.0, 2.0, 3.0])
        v2 = Vector([0.0, 10.0, -100.0])
        print(f"v1 = {v1.__str__()}")
        print(f"v1 = {v2.__str__()}")
        print("coef = [10.0, -2.0]")
        res = linear_combination([v1, v2], [10.0, -2.0])
        self.assertEqual(res.data, [10.0, 0.0, 230.0])
        print(f"result = {res.__str__()}\n")

        w1 = Vector([1.0, 5.0, -1.0])
        w2 = Vector([1.0, 2.0, 1.0])
        w3 = Vector([1.0, 4.0, 3.0])
        coef = [1.0, -2.0, 3.0]
        print(f"w1 = {w1.__str__()}")
        print(f"w2 = {w2.__str__()}")
        print(f"w3 = {w3.__str__()}")
        print(f"coef = {coef}")
        res = linear_combination([w1, w2, w3], coef)
        self.assertEqual(res.data, [2.0, 13.0, 6.0])
        print(f"result = {res.__str__()}\n")

        x1 = Vector(
            [
                0.0,
                0.0,
                0.0,
            ]
        )
        x2 = Vector(
            [
                0.0,
                0.0,
                0.0,
            ]
        )
        coef = [1.0, 2.0, 3.0]
        print(f"x1 = {x1.__str__()}")
        print(f"x2 = {x2.__str__()}")
        print(f"coef = {coef}")
        try:
            self.assertEqual(
                linear_combination([x1, x2], coef),
                "cannot compute linear combination of vector if size u doesn't match with size of coef",
            )
        except ValueError as error:
            print(f"ValueError: {error}")
