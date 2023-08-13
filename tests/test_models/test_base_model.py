#!/usr/bin/python3
"""This module define a Python unittest for base_model.py

Unittest classes:
    base_model__Public_instance
    base_model__save
    base_model__to_dict

"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
import datetime
import pycodestyle


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """creat an instance of BaseModel"""
        self.base = BaseModel()

    def test_instance_creation(self):
        """unittest the BaseModel intance creation and
        Public instance attributes setting
        """
        self.assertIsInstance(self.base, BaseModel)
        self.assertTrue(hasattr(self.base, 'id'))
        self.assertTrue(hasattr(self.base, 'created_at'))
        self.assertTrue(hasattr(self.base, 'updated_at'))

    def test_str_method(self):
        """unittest the str method"""
        expected_str = "[BaseModel] ({}) {}".format(self.base.id,
                                                    self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    @patch('models.storage.save')
    def test_save_method(self, mock_save):
        """unittest save method && updated_at set"""
        self.base.save()
        self.assertTrue(hasattr(self.base, 'updated_at'))
        self.assertTrue(mock_save.called)

    def test_to_dict_method(self):
        """unittest to_dict method valid dictionary representation
        """
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIn('__class__', base_dict)
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(self.base.id, base_dict['id'])
        self.assertEqual(self.base.created_at.isoformat(),
                         base_dict['created_at'])
        self.assertEqual(self.base.updated_at.isoformat(),
                         base_dict['updated_at'])

    def test_pycodestyle(self):
        """unittest to test pycodestyle compliance"""
        style_guide = pycodestyle.StyleGuide()
        result = style_guide.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
