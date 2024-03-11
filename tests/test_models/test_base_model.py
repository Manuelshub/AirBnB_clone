#!/usr/bin/python3
"""
This module contains all the testcases for BaseModel class.
"""
from datetime import datetime
from models.base_model import BaseModel
import os
from time import sleep
import unittest



class TestBaseModel_instantiating(unittest.TestCase):
    """
    Unittest method for testing instatiation of the class BaseModel
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

    def test_instantiates_with_no_args(self):
        """Checks if the class is the same type as the instance BaseModel()"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """
        This method tests if an object has an id attribute.
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


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of BaseModel"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.10)
        first_update = bm.updated_at
        bm.save()
        self.assertLess(first_update, bm.updated_at)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bm_id = "BaseModel." + bm.id
        with open("file.json") as file:
            self.assertIn(bm_id, file.read())

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.10)
        first_update = bm.updated_at
        bm.save()
        second_update = bm.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.10)
        bm.save()
        self.assertLess(second_update, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for the to_dict method"""

    def test_type_of_to_dict(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_attr(self):
        bm = BaseModel()
        bm.name = "Alx"
        bm.my_number = 1024
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_contrast_to_dict_and_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_contains_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_type_datetime_attributes(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict['created_at']))
        self.assertEqual(str, type(bm_dict['updated_at']))


if __name__ == "__main__":
    unittest.main()
