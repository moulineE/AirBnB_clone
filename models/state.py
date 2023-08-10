#!/usr/bin/python3
"""Module for the State class
Contains the State class for the AirBnB clone
"""
from models.base_model import BaseModel


class State(BaseModel):
    """a class State that inherits from BaseModel
    that represent a State

    Attributes:
        name (str): the state name
    """

    name = ''
