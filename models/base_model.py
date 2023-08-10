#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""
import uuid
import datetime


class BaseModel:
    """
    The BaseModel class represents a fundamental data model.

    Attributes:
        id : A unique identifier for each instance.
        created_at : The timestamp when the instance is created.
        updated_at : The timestamp when the instance is last updated.
    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """
        Initialize a BaseModel instance.

        Args:
            id : The unique identifier for the instance.
                Defaults to a new UUID.
            created_at : The timestamp of creation.
                Defaults to the current datetime.
            updated_at : The timestamp of the last update.
                Defaults to created_at.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: A formatted string with the class name, id, and attributes.
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict
