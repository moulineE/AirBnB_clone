#!/usr/bin/python3
"""Module for the amenity class
Contains the amenity class for the AirBnB clone
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """a class Amenity that inherits from BaseModel
    that represent the disponible amenity

    Attributes:
        name (str): the Amenity name
    """

    name = ''
