#!/usr/bin/python3
"""Module for the City class
Contains the City class for the AirBnB clone
"""
from models.base_model import BaseModel


class City(BaseModel):
    """a class City that inherits from BaseModel
    that represent a city

    Attributes:
        state_id (str) : the city state id
        name: (str) the name of the city
    """

    state_id = ''
    name = ''
