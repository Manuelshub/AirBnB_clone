#!/usr/bin/python3

"""
A module that contains a class review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
