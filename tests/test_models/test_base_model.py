#!/usr/bin/env python3
"""
importing the modules
"""
import unittest
from models.base_model import BaseModel
import datetime

class TestBasemodel(unittest.TestCase):
    """
    Test for base_model
    """

    def test_for_ids(self):
        """
        Test for different id
        """
        id_check = BaseModel()
        id_check2 = BaseModel()
        # checks if the ids are equal
        self.assertNotEqual(id_check.id, id_check2.id)

    def test_created_at_updated_at(self):
        """
        Test to checks if both are data objects
        """
        models = BaseModel()
        self.assertIsInstance(models.created_at, datetime.datetime)
        self.assertIsInstance(models.updated_at, datetime.datetime)

    def test_for_to_dict(self):
        """
        Test for the to_dict method
        """
        model = BaseModel()
        model_dict = model.to_dict()
        # to check if class is in the dictonary
        self.assertIn('__class__', model_dict)
        # check if created_at and updated_at are strings
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
