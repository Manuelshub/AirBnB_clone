#!/usr/bin/python3

"""
This module contains a class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
