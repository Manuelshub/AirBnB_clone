#!/usr/bin/python3
"""
This module contains a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances:
"""
from models.base_model import BaseModel
from models.user import User
import json
import os


class FileStorage:

    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances:

    Attributes:
        __file_path: path to a json file
        __objects: a dictionary that stores all objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        A method that returns __object
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        A method that sets in __object the obj.
        Args:
            obj: the object to be set in the dictionary
        """
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_cls_name}.{obj.id}"] = obj

    def save(self):
        """
        This method serializes __objects to a JSON file
        """
        obdict = FileStorage.__objects
        ob_dict = {key: val.to_dict() for key, val in obdict.items()}
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(ob_dict))

    def reload(self):
        """
        Deserializes a JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                ob_dict = json.load(f)
                for key, val in ob_dict.items():
                    cls_name, ob_id = key.split('.')
                    cls = eval(cls_name)
                    obj = cls(**val)
                    self.new(obj)
