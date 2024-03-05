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
        print(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")


