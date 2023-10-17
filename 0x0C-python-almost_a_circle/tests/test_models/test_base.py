#!/usr/bin/python3
"""unit tests for base.py"""
from unittest import TestCase

import pep8
from models.base import Base


class TestBase(TestCase):
    def test_pep8(self):
        """pep8 test"""
        style = pep8.StyleGuide(quiet=True)
        file = style.check_files(["models/base.py"]).total_errors
        self.assertEqual(file, 0, "Found code style errors (and warnings).")

    def test_id(self):
        """ids test"""
        self.assertTrue(Base(7), self.id == 7)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(-1), self.id == -1)

    def test_id_increment(self):
        """id increment test"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_to_json_string(self):
        """to json str test"""
        self.fail()

    def test_save_to_file(self):
        """save to json file test"""
        self.fail()

    def test_from_json_string(self):
        """from json str test"""
        self.fail()

    def test_create(self):
        """create test"""
        self.fail()

    def test_load_from_file(self):
        """load from json file test"""
        self.fail()

    def test_save_to_file_csv(self):
        """save to csv file test"""
        self.fail()

    def test_load_from_file_csv(self):
        """load from csv file test"""
        self.fail()
