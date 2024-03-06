#!/usr/bin/python3

"""
This module contains a class FileStorage that serializes instances 
to a JSON file and deserializes JSON file to instances:
"""

class FileStorage:

    """
    This class serializes instances to a JSON file and 
    deserializes JSON file to instances:

    Attributes:
        __file_path: path to a json file
        __objects: a dictionary that stores all objects
    """

    __file_path = ""
    __objects = {}

    def all(self):
        """
        A method that returns __object
        """
        return self.__objects

    def new(self, obj):
        """
        A method that sets in __object the obj.
        Args:
            obj: the object to be set in the dictionary
        """

