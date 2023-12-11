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
        print("\n[vector]")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.YELLOW)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_utils(self):
        """test utilitary functions
        - get_size()
        - __str__()
        - reshape()
        """
        test = Vector([1.0, 1.0])
        self.assertEqual(test.__str__(), "[1.0, 1.0]")
        self.assertEqual(test.get_size(), 2)
        try:
            empty = Vector([])
            print(empty)
        except TypeError as error:
            print(f"TypeError: {error}")

        test_reshape = Vector([1, 2, 3, 4, 5, 6])
        self.assertEqual(test_reshape.reshape(2, 3), [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        try:
            self.assertEqual(
                test_reshape.reshape(2, 2), [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
            )
        except ValueError as error:
            print(f"ValueError: {error}")

    def test_add(self):
        """test add a vector"""
        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} + {v.__str__()}")
        u.add(v)
        self.assertEqual(u.data, [7.0, 10.0])
        print(f"u = {u.__str__()}\n")

        u = Vector([2.0])
        v = Vector([5.0, 7.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} + {v.__str__()}")
        try:
            self.assertEqual(u.add(v), Vector([7.0, 10.0]))
        except ValueError as error:
            print(f"ValueError: {error}")

    def test_subtract(self):
        """test substract a vector"""
        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} + {v.__str__()}")
        u.sub(v)
        self.assertEqual(u.data, [-3.0, -4.0])
        print(f"u = {u.__str__()}\n")

        u = Vector([2.0])
        v = Vector([5.0, 7.0])
        print(f"u = {u.__str__()}")
        print(f"v = {v.__str__()}")
        print(f"u = {u.__str__()} + {v.__str__()}")
        try:
            self.assertEqual(u.sub(v), [-3.0, -4.0])
        except ValueError as error:
            print(f"ValueError: {error}")

    def test_scale(self):
        """test multiply a vector by a scalar"""
        u = Vector([2.0, 3.0])
        print(f"u = {u.__str__()} * 2")
        u.scl(2.0)
        self.assertEqual(u.data, [4.0, 6.0])
        print(f"u = {u.__str__()}")


class TestMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n[Exercice 00] add, substract and scale")
        print("----------------------------------------------------------------------")
        print("\n[matrix]")
        print("----------------------------------------------------------------------")

    def setUp(self):
        print(Fore.LIGHTCYAN_EX)
        print(self.shortDescription())
        print(Fore.RESET)

    def test_utils(self):
        """test utilitary functions
        - get_shape()
        - __str__()
        - reshape()
        - is_square()
        """
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        print(f"Matrix:\n{u.__str__()}")
        self.assertEqual(u.get_shape(), (2, 2))
        self.assertEqual(u.is_square(), True)

        reshaped = u.reshape()
        print("reshaped matrix to one dimensional vector:", reshaped)
        self.assertEqual(reshaped, [1.0, 2.0, 3.0, 4.0])

    def test_add(self):
        """test add a matrix"""
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        print(f"Matrix u:\n{u.__str__()}")
        print(f"Matrix v:\n{v.__str__()}")
        u.add(v)
        self.assertEqual(u.data, [[8.0, 6.0], [1.0, 6.0]])
        print(f"Matrix u + Matrix v:\n{u.__str__()}")

        u = Matrix([[1.0], [3.0]])
        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        print(f"Matrix u:\n{u.__str__()}")
        print(f"Matrix v:\n{v.__str__()}")
        try:
            self.assertEqual(u.add(v), [[8.0, 6.0], [1.0, 6.0]])
        except ValueError as error:
            print(f"ValueError: {error}")

    def test_subtract(self):
        """test substract a matrix"""
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        print(f"Matrix u:\n{u.__str__()}")
        print(f"Matrix v:\n{v.__str__()}")
        u.sub(v)
        self.assertEqual(u.data, [[-6.0, -2.0], [5.0, 2.0]])
        print(f"Matrix u - Matrix v:\n{u.__str__()}")

    def test_scale(self):
        """test multiply a matrix by a scalar"""
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        print(f"Matrix u:\n{u.__str__()}")
        u.scl(2.0)
        self.assertEqual(u.data, [[2.0, 4.0], [6.0, 8.0]])
        print(f"Matrix u * 2:\n{u.__str__()}")
