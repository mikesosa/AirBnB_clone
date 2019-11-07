#!/usr/bin/python3
"""
==============================================
Base class mother of all classes and chikens
==============================================
"""

import uuid
from datetime import datetime


class BaseModel:
    """Mother of classes and chickens"""

    def __init__(self):
        """The constructor"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print information """
        string = "[" + type(self).__name__ + "]"
        string += " (" + self.id + ") " + str(self.__dict__)
        return string

    def save(self):
        """update the attribute updated_at"""
        self.update_at = datetime.now()

    def to_dict(self):
        """save in a dictionary"""

        my_dic = {}
        for key, value in self.__dict__.items():
            my_dic["__class__"] = self.__class__.__name__
            if key == "created_at" or key == "updated_at":
                my_dic[key] = value.isoformat()
            else:
                my_dic[key] = value
        return my_dic
