#!/usr/bin/python3
"""
This module defines FileStorage class
that serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serial_obj = {}
        for key, value in self.__objects.items():
            serial_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(serial_obj, f)

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside."""
        if obj:
            self.__objects.pop(f"{obj.__class__.__name__}.{obj.id}", None)
            self.save()

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    value = eval(key.split(".")[0])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
