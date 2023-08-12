#!/usr/bin/python3
"""Module for the User class
Contains the User class for the AirBnB clone
Need to Update FileStorage to manage correctly serialization
and deserialization of User.
&& Update interpreter (console.py) to allow show, create,
destroy, update and all used with User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """a class User that inherits from BaseModel
    that represent a User

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
