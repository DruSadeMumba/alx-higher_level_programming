#!/usr/bin/python3
"""unit tests for square.py"""
from unittest import TestCase

import pep8


class TestSquare(TestCase):
    """Square class tests"""
    def test_pep8(self):
        """pep8 test"""
        style = pep8.StyleGuide(quiet=True)
        file = style.check_files(["models/square.py"]).total_errors
        self.assertEqual(file, 0, "Found code style errors (and warnings).")

    def test_size(self):
        """size test"""
        self.fail()

    def test_update(self):
        """update func test"""
        self.fail()

    def test_to_dictionary(self):
        """to dict func test"""
        self.fail()
