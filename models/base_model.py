#!/usr/bin/python3
"""This module define a BaseModel class"""
import uuid
import datetime


class BaseModel:
    """the basemodel class"""

    def __init__(self, id=None, created_at=None, updated_at=None):
        """class constructor

        Args:
            id
            created_at
            updated_at

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """overriding the __str__ method"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        placeholder !!!
        """
        pass
