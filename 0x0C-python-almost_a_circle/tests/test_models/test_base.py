#!/usr/bin/python3
"""unit tests for base.py"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """base class tests"""
    def test_pep8(self):
        """pep8 test"""
        style = pep8.StyleGuide(quiet=True)
        file = style.check_files(["models/base.py"]).total_errors
        self.assertEqual(file, 0, "Found code style errors (and warnings).")

    def test_id_given(self):
        """Test ids match when given"""
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-80), self.id == -80)

    def test_id_not_given(self):
        """Test ids match incremented nb_objects when not given"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
