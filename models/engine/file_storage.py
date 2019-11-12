#!/usr/bin/python3
"""
============================================
Module for serialization/deserealization JSON
============================================
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """class for serialization/deserealization JSON"""

    def __init__(self):
        """the constructor"""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns all objects storage in the file"""
        return self.__objects

    def new(self, obj):
        """sets a new object"""

        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """serialize objects in json file"""
        # print(self.__objects)   
        # for k, v in self.__objects.items():
        #     with open(self.__file_path, mode='w', encoding='utf-8') as f:
        #         f.write(json.dumps({k: v.to_dict()}))
        my_dict = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            for k, v in self.__objects.items():
                my_dict[k] = v.to_dict()
            f.write(json.dumps(my_dict))
        # print("======")
        # print(my_dict)
        # print("======")
        # print(json.dumps(my_dict))
        # print("======")
        # print("entro a save")
        # print(self.__objects)

    def reload(self):
        """deserialize objects in json file"""
        # pass
        """ deserializes the JSON file to __objects, if path exists or do
        nothing. no exceptions should raise """
        # create a Dict that matched keys with values
        # keys are strings and values are the classes of the values
        obj_dict = {"BaseModel": BaseModel}
        # check if the file is even there first

        # check if the file is even there first
        if os.path.isfile(self.__file_path):
            # attempt to open that file and load the string that we read

            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                x = json.loads(f.read())
                for k, v in x.items():
                    # print (x)
                    self.__objects[k] = obj_dict[v["__class__"]](**v)
                    # print(self.__objects)
                # We read a dict, we iterate or enumerate through it
                # We make a new __object[key] in file storage that
                # Does access magic with the obj_dict. stores in the data
                # It works. You jut need to believe

# class Perro:
#     def __init__(self):
#         self.id = 123
#         self.name = 'mike'

#     def __str__(str):
#         return str(self.__dict__)


#     def to_dict(self):
#         """save in a dictionary"""

#         my_dic = {}
#         for key, value in self.__dict__.items():
#             my_dic["__class__"] = self.__class__.__name__
#             my_dic[key] = value
#         return my_dic

# a = Perro()
# m = FileStorage()
# m.new(a)
# m.save()
# m.reload()