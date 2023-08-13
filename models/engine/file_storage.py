#!/usr/bin/python3
"""Module for File_storage class
Contains the file_storage class for the AirBnB clone console.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """a Filestorage class represents a json storage engine
    Attributes:
        __file_path (str): path to the JSON file (ex: file.json)
        __objects (sict): empty but will store all objects by <class name>.id
            with id=12121212, the key will be BaseModel.12121212)

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            serialized_objs = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(serialized_objs, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    FileStorage.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            return
