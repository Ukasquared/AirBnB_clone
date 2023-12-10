#!/usr/bin/env python3
""" filestorage module"""
import json
from models.base_model import BaseModel

class FileStorage:
    """serializes instances to JSON
    file and deserializes Json files
    to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns all the saved object"""
        return self.__objects
    
    def new(self, obj):
        """add key value pairs to __object"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """save serialized dictionary in a file"""
        new_dicts = {}
        for key, value in self.__objects.items():
            new_dicts[key] = value.to_dict()
        with open(self.__file_path, 'w') as file_string:
            json.dump(new_dicts, file_string)
    
    def reload(self):
        """ deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, 'r') as file_string:
                objects = json.load(file_string)
                for key, value in objects.items():
                    obj = BaseModel(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass