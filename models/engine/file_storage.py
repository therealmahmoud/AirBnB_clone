#!/usr/bin/python3
"""A file_storage file which serializes instances to
a JSON file and deserializes JSON file to instances."""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


allw_cls = {"BaseModel": BaseModel, "User": User, "Place": Place,
            "State": State, "City": City, "Amenity": Amenity, "Review": Review}


class FileStorage:
    """Serializes instances to a
    JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary containing all serialized objects.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""

        dict_to_json = {}
        for key, value in self.__objects.items():
            dict_to_json[key] = value.to_dict()
            with open(self.__file_path, 'w') as json_file:
                json.dump(dict_to_json, json_file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, 'r') as json_file:
                dic_obj = json.load(json_file)
                for key, value in dic_obj.items():
                    class_name = key.split(".")[0]
                    if class_name in allw_cls:
                        self.__objects[key] = eval(class_name)(**value)
                    else:
                        pass
        except FileNotFoundError:
            return
