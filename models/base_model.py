#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""
import uuid
import datetime
import models


class BaseModel:
    """The BaseModel class represents a fundamental data model."""

    def __init__(self, *args, **kwargs):
	"""Initialization of a Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
	    if kwargs:  # If kwargs is not empty
		    for key, value in kwargs.items():
			    if key == 'created_at' or key == 'updated_at':
				    setattr(self, key, datetime.datetime.strptime(value,
										  '%Y-%m-%dT%H:%M:%S.%f'))
			    elif key != '__class__':
				    setattr(self, key, value)
			    else:  # If kwargs is empty
				    self.id = str(uuid.uuid4())
				    self.created_at = datetime.datetime.now()
				    self.updated_at = self.created_at
				    models.storage.new(self)
				    
    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict	
