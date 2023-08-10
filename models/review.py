#!/usr/bin/python3
"""Module for the Review class
Contains the Review class for the AirBnB clone
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """a class Review that inherits from BaseModel
    that represent the Review

    Attributes:
        place_id (str): the place id of the review (Place.id)
        user_id (str): the user id of the review (User.id)
        text (str): the review string
    """

    place_id = ''
    user_id = ''
    text = ''
