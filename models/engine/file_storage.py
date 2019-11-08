#!/usr/bin/python3
"""
============================================
Module for serialization/deserealization JSON
============================================
"""

import json
import os


class FileStorage:
    """class for serialization/deserealization JSON"""

    def  __init__(self):
        """the constructor"""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns all objects storage in the file"""

        return self.__objects

    def new(self, obj):
        """sets a new object"""

        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj.to_dict()

    def save(self):
        """serialize objects in json file"""

        with open(self.__file_path, mode = 'w', encoding = 'utf-8') as f:
           self.__file_path = f.write(json.dumps(self.__objects))

    def reload(self):
        """deserialize objects in json file"""

        if os.path.isfile(self.__file_path):
            print("si existe")
            with open(self.__file_path) as f:
                to_json = f.read()
            self.__objects = json.loads(to_json)


m = FileStorage()

class Perruno:
    def __init__(self):
        self.name = "yesid"
        self.id = "123456"
        m.new(self)
        m.save()
        m.reload()

    def to_dict(self):
        my_dick = {}
        for key, value in self.__dict__.items():
            my_dick[key] = value
        return my_dick

    def __str__(self):
        return str(self.__dict__)

x = Perruno()
