#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest for max int"""
    def test_module_docstring(self):
        mod = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod) > 1)

    def test_function_docstring(self):
        func = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def test_None(self):
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]), None)

    def test_list(self):
        self.assertEqual(max_integer([[1, 2], [2, 3]]), [2, 3])

    def test_string_list(self):
        self.assertEqual(max_integer("1234"), '4')
        self.assertEqual(max_integer("abc"), 'c')
        self.assertEqual(max_integer(["12", "34", '56']), '56')
        self.assertIsNot(max_integer(["1234"]), '4')

    def test_int_float(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1.0, 1.1, 1.2]), 1.2)
        self.assertEqual(max_integer([{4, 3}, {2}, {1}]), {4, 3})

    def test_err(self):
        with self.assertRaises(TypeError):
            max_integer(["abc", {1, 2}])
        with self.assertRaises(TypeError):
            max_integer([None, True])
        with self.assertRaises(TypeError):
            max_integer({1}, {2, 3, 4})


if __name__ == "__main__":
    unittest.main()
