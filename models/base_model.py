#!/usr/bin/python3
"""creating a class that defines all
common attributes/methods for other classes"""

import uuid
from datetime import datetime
import json
import models


class BaseModel:
    """BaseModel class, used to meet the
    docstring description above"""
    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, dt_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ str representation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        new_dicts = self.__dict__.copy()
        new_dicts["__class__"] = self.__class__.__name__
        new_dicts["created_at"] = self.created_at.isoformat()
        new_dicts["updated_at"] = self.updated_at.isoformat()
        return new_dicts

    def delete(self):
        """Delete method"""
        models.storage.delete(self)
