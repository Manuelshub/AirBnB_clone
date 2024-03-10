#!/usr/bin/python3
"""
This module contains all the testcases for BaseModel class.
"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    This class contains methods tests the class BaseModel
    """
    def setUp(self):
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()
        self.to_dict = self.bm1.to_dict()
        self.bm3 = BaseModel(**self.to_dict)

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertIsInstance(self.bm2, BaseModel)

    def test_id(self):
        """
        This method tests if an object has an id attr
        """
        self.assertTrue(hasattr(self.bm1, 'id'))
        self.assertTrue(hasattr(self.bm2, 'id'))

    def test_update_and_create(self):
        """
        This tests if the object has updated_at and created_at attr
        """
        self.assertTrue(hasattr(self.bm1, 'updated_at'))
        self.assertTrue(hasattr(self.bm1, 'created_at'))
        self.assertTrue(hasattr(self.bm2, 'updated_at'))
        self.assertTrue(hasattr(self.bm2, 'created_at'))

    def test_id_is_same(self):
        """
        This test if the id of two instances are the same.
        """
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertIsNot(self.bm1.id, self.bm2.id)

    def created_at(self):
        """
        This method tests if the created_at of both objects are the same.
        """
        self.assertNotEqual(self.bm1.created_at, self.bm2.created_at)

    def test_updated_at(self):
        """
        This method tests if the updated_at of both objects are the same.
        """
        self.assertNotEqual(self.bm1.updated_at, self.bm2.updated_at)
        old = self.bm1.updated_at
        self.bm1.save()
        self.assertNotEqual(old, self.bm1.updated_at)

    def test_to_dict(self):
        """
        This method checks if variable is of type dictionary
        """
        self.to_dict = self.bm1.to_dict()
        self.assertIsInstance(self.to_dict, dict)

    def test_new_kwargs_instance(self):
        """
        This method creates a new object with a dictionary as
        argument.
        """
        self.assertEqual(self.bm3.id, self.bm1.id)

    def test_id_type(self):
        """
        This method checks for the type of all object's id
        """
        self.assertIsInstance(self.bm3.id, str)
        self.assertIsInstance(self.bm2.id, str)
        self.assertIsInstance(self.bm1.id, str)

    def test_updated_at_type(self):
        """
        This checks for the type of the attribute updated_at
        """
        self.assertNotIsInstance(self.bm3.updated_at, str)
        self.assertIsInstance(self.bm3.updated_at, datetime)

    def test_kwargs_obj_check(self):
        """
        This method checks if an object that has it's arguments
        from another object is the same.
        """
        self.assertIsNot(self.bm3, self.bm1)


if __name__ == "__main__":
    unittest.main()
