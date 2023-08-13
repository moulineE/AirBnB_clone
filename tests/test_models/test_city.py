#!/usr/bin/python3
"""This module define a Python unittest for city.py

Unittest classes:
    TestCity

"""

import unittest
from models.city import City
import datetime
import pycodestyle


class TestCity(unittest.TestCase):

    def setUp(self):
        """creat an instance of City"""
        self.city = City()

    def test_instance_creation(self):
        """unittest the City intance creation and
        attributes setting
        """
        self.assertIsInstance(self.city, City)
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_attribute_types(self):
        """nittest if attrs is of type str"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_str_method(self):
        """test BaseModel _str_method with City"""
        expected_str = "[City] ({}) {}".format(self.city.id,
                                               self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict_method(self):
        """unittest if BaseModel to_dict_method is valid"""
        self.city.state_id = "my statr id"
        self.city.name = "my city name"
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(self.city.id, city_dict['id'])
        self.assertEqual(self.city.created_at.isoformat(),
                         city_dict['created_at'])
        self.assertEqual(self.city.updated_at.isoformat(),
                         city_dict['updated_at'])
        self.assertEqual(self.city.state_id, city_dict['state_id'])
        self.assertEqual(self.city.name, city_dict['name'])

    def test_pycodestyle(self):
        """unittest to test pycodestyle compliance"""
        style_guide = pycodestyle.StyleGuide()
        result = style_guide.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
