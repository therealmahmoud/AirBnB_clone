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
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""

        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(dict_to_json, json_file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                dic_obj = json.load(json_file)
                for value in dic_obj.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return
