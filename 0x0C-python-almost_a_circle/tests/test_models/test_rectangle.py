#!/usr/bin/python3
"""unit tests for rectangle.py"""
from unittest import TestCase

import pep8


class TestRectangle(TestCase):
    """Rectangle class tests"""
    def test_pep8(self):
        """pep8 test"""
        style = pep8.StyleGuide(quiet=True)
        file = style.check_files(["models/rectangle.py"]).total_errors
        self.assertEqual(file, 0, "Found code style errors (and warnings).")

    def test_width(self):
        """width test"""
        self.fail()

    def test_height(self):
        """height test"""
        self.fail()

    def test_x(self):
        """x test"""
        self.fail()

    def test_y(self):
        """y test"""
        self.fail()

    def test_area(self):
        """area func test"""
        self.fail()

    def test_display(self):
        """display func test"""
        self.fail()

    def test_update(self):
        """update func test"""
        self.fail()

    def test_to_dictionary(self):
        """to dict func test"""
        self.fail()
