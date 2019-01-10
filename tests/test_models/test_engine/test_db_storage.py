#!/usr/bin/python3
"""test for db storage"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


class TestDbStorage(unittest.TestCase):
    """this will test the db_storage"""
    """
    def test_pep8_db(self):

        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["db_storage.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')
    """
    def test_docstrings_in_db(self):
        """checking for docstrings"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage. __init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

if __name__ == "__main__":
    unittest.main()
