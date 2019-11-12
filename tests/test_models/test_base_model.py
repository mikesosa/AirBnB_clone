#!/usr/bin/python3
"""Base_model unittest module"""

import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
# from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_base_model(self):
        """testing the BaseModel"""
        dog = BaseModel()
        self.assertIs(type(dog.id), str)
        self.assertIs(type(dog.created_at), datetime)
        self.assertIs(type(dog.updated_at), datetime)
        self.assertNotEqual(dog.created_at, dog.updated_at)
        # self.assertFalse(dog.updated_at == datetime.utcnow())
        # old_updated = dog.updated_at
        dog.save()

    def test_save_model(self):
        """ tests to see if the return type of save is a string """
        dog = BaseModel()
        dog.save()
        self.assertIsInstance(dog.to_dict()['created_at'], str)
        self.assertIsInstance(dog.to_dict()['updated_at'], str)


if __name__ == '__main__':
    unittest.main()







#         self.assertNotEqual(old_updated, dog.updated_at)
#         d = dog.to_dict()
#         self.assertEqual(type(d), dict)
#         self.assertEqual(d['__class__'], "BaseModel")
#         self.assertEqual(d['created_at'], dog.created_at.isoformat())
#         self.assertEqual(d['updated_at'], dog.updated_at.isoformat())
#         self.assertEqual(d['id'], dog.id)

#     def test_init_with_dict(self):
#         """testing init method"""
#         dd = {"id": "123-123-123",
#               "key1": "val1", "key2": "val2", "key3": "val3"}
#         b = BaseModel(**dd)
#         self.assertEqual(b.id, "123-123-123")
#         self.assertEqual(b.key1, "val1")
#         self.assertEqual(b.key2, "val2")
#         self.assertEqual(b.key3, "val3")

#     def test_save_is_dict(self):
#         """ tests to see if the return type of save is a string """
#         dog = BaseModel()
#         dog.save()
#         self.assertIsInstance(dog.to_dict()['created_at'], str)
#         self.assertIsInstance(dog.to_dict()['updated_at'], str)

#     def test_has_attr(self):
#         """ tests if the base model has the attr """
#         self.assertTrue(hasattr(BaseModel, "save"))
#         # save(self)
#         self.assertTrue(hasattr(BaseModel, "__init__"))
#         self.assertTrue(hasattr(BaseModel, "to_dict"))

#     def test_doc_strings(self):
#         """ tests if there are doc strings to all methods """
#         self.assertTrue(BaseModel.__doc__)
#         self.assertTrue(BaseModel.save.__doc__)
#         self.assertTrue(BaseModel.to_dict.__doc__)