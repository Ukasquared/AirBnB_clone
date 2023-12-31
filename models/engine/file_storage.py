#!/usr/bin/python3
""" filestorage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes instances to JSON
    file and deserializes Json files
    to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns all the saved object"""
        # we  need make it accessble by all methods
        # I changed from self to FileStorage.
        return self.__objects

    def new(self, obj):
        """add key value pairs to __object"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        # same thing here, we need make it available to all
        self.__objects[key] = obj

    def classes(self):
        """classes with their
        names
        """
        class_names = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
            "City": City,
            "State": State
        }
        return class_names

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
                    if value["__class__"] in self.classes().keys():
                        obj_class = self.classes()[value["__class__"]]
                        obj = obj_class(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
