#!/usr/bin/python3
"""
This module contains a class BaseModel that defines all common attributes
and methods for other classes.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    This class defines all common attributes and methods for other classes
    """

    def __init__(self):
        """
        This is the constructor method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        This method prints a string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates a public instance attr with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This method returns a dictionary of an instance
        """
        cls_name = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        self.__dict__['__class__'] = cls_name
        return self.__dict__
