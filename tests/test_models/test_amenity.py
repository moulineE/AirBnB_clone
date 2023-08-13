#!/usr/bin/python3
"""This module define a Python unittest for amenity.py

Unittest classes:
    TestAmenity

"""


import unittest
from models.amenity import Amenity
import datetime
import pycodestyle


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """creat an instance of Amenity"""
        self.amenity = Amenity()

    def test_instance_creation(self):
        """unittest the Amenity intance creation and
        attributes setting
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_attribute_types(self):
        """unittest if name is a str"""
        self.assertIsInstance(self.amenity.name, str)

    def test_str_method(self):
        """test BaseModel _str_method with Amenity """
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id,
                                                  self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        """unittest if BaseModel to_dict_method is valid"""
        self.amenity.name = "tester"
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(self.amenity.id, amenity_dict['id'])
        self.assertEqual(self.amenity.created_at.isoformat(),
                         amenity_dict['created_at'])
        self.assertEqual(self.amenity.updated_at.isoformat(),
                         amenity_dict['updated_at'])
        self.assertEqual(self.amenity.name, amenity_dict['name'])

    def test_pycodestyle(self):
        """unittest to test pycodestyle compliance"""
        style_guide = pycodestyle.StyleGuide()
        result = style_guide.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
