#!/usr/bin/python3
"""
This module contains a class BaseModel that defines all common attributes
and methods for other classes.
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    This class defines all common attributes and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        This is the constructor method
        """
        str_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        lst = ["updated_at", "created_at"]
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in lst:
                        setattr(self, key, datetime.strptime(value, str_fmt))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """
        This method returns a dictionary of an instance
        """
        dict_copy = self.__dict__.copy()
        cls_name = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()

        dict_copy['__class__'] = cls_name
        return dict_copy
