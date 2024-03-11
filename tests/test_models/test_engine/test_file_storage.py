#!/usr/bin/python3
"""Unittests for the Filestorage class"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
import models
import os
import unittest


class TestFileStorage_instantiating(unittest.TestCase):
    """Unittests for testing instantiating the class"""

    def test_filestorage_instantiating(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_type_of_storage(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_filestorage_intantiating_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_filestorage_file_path_is_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_filestorage_objects_is_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

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
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        ur = User()
        st = State()
        pc = Place()
        ct = City()
        ay = Amenity()
        rw = Review()
        models.storage.new(bm)
        models.storage.new(ur)
        models.storage.new(st)
        models.storage.new(pc)
        models.storage.new(ct)
        models.storage.new(ay)
        models.storage.new(rw)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + ur.id, models.storage.all().keys())
        self.assertIn(ur, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pc.id, models.storage.all().keys())
        self.assertIn(pc, models.storage.all().values())
        self.assertIn("City." + ct.id, models.storage.all().keys())
        self.assertIn(ct, models.storage.all().values())
        self.assertIn("Amenity." + ay.id, models.storage.all().keys())
        self.assertIn(ay, models.storage.all().values())
        self.assertIn("Review." + rw.id, models.storage.all().keys())
        self.assertIn(rw, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bm = BaseModel()
        ur = User()
        st = State()
        pc = Place()
        ct = City()
        ay = Amenity()
        rw = Review()
        models.storage.new(bm)
        models.storage.new(ur)
        models.storage.new(st)
        models.storage.new(pc)
        models.storage.new(ct)
        models.storage.new(ay)
        models.storage.new(rw)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + ur.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pc.id, save_text)
            self.assertIn("City." + ct.id, save_text)
            self.assertIn("Amenity." + ay.id, save_text)
            self.assertIn("Review." + rw.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        ur = User()
        st = State()
        pc = Place()
        ct = City()
        ay = Amenity()
        rw = Review()
        models.storage.new(bm)
        models.storage.new(ur)
        models.storage.new(st)
        models.storage.new(pc)
        models.storage.new(ct)
        models.storage.new(ay)
        models.storage.new(rw)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + ur.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pc.id, objs)
        self.assertIn("City." + ct.id, objs)
        self.assertIn("Amenity." + ay.id, objs)
        self.assertIn("Review." + rw.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
