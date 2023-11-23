#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 20)

    def test_unordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_unordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([23, 58, 91, 24, 1024, 89, 98,
                                     108, 256, 512]), 1024)

    def test_positives_and_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 108, -256, -512]),
            108)
