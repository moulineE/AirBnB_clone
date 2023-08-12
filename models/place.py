#!/usr/bin/python3
"""Module for the Place class
Contains the Place class for the AirBnB clone
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """a class Place that inherits from BaseModel
    that represent a Place

    Attributes:
        city_id (str):the place city id (city.id)
        user_id (str): the user id (User.id)
        name (str): the Place name
        description (str): the place description
        number_rooms (int): number of room of the place
        number_bathroom (int): number of bathroom of the place
        max_guest (int): numer of maximum guest in the place
        price_by_night (int): price of a night in the place
        latitude (float) latitude of the place
        longitude (float) longitude of the place
        amenity_ids (list) list of strigs of amenity id (Amenity.id)

    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
