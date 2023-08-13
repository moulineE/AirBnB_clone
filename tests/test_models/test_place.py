#!/usr/bin/python3
"""This module define a Python unittest for place.py

Unittest classes:
    TestPlace

"""

import unittest
from models.place import Place
import datetime
import pycodestyle


class TestPlace(unittest.TestCase):

    def setUp(self):
        """creat an instance of Place"""
        self.place = Place()

    def test_instance_creation(self):
        """unittest the City intance creation and
        attributes setting
        """
        self.assertIsInstance(self.place, Place)
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))

    def test_attribute_types(self):
        """unittest if attrs is of the correct type"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_str_method(self):
        """test BaseModel _str_method with Place"""
        expected_str = "[Place] ({}) {}".format(self.place.id,
                                                self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict_method(self):
        """unittest if BaseModel to_dict_method is valid"""
        self.place.city_id = "a city id"
        self.place.user_id = "a user id"
        self.place.name = "the place name"
        self.place.description = "the place desc"
        self.place.number_rooms = 10
        self.place.number_bathrooms = 3
        self.place.max_guest = 30
        self.place.price_by_night = 1000
        self.place.latitude = 0.1
        self.place.longitude = 0.1
        self.place.amenity_ids = ["hello", "idlist"]
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('__class__', place_dict)
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(self.place.id, place_dict['id'])
        self.assertEqual(self.place.created_at.isoformat(),
                         place_dict['created_at'])
        self.assertEqual(self.place.updated_at.isoformat(),
                         place_dict['updated_at'])
        self.assertEqual(self.place.city_id, place_dict['city_id'])
        self.assertEqual(self.place.user_id, place_dict['user_id'])
        self.assertEqual(self.place.name, place_dict['name'])
        self.assertEqual(self.place.description, place_dict['description'])
        self.assertEqual(self.place.number_rooms, place_dict['number_rooms'])
        self.assertEqual(self.place.number_bathrooms,
                         place_dict['number_bathrooms'])
        self.assertEqual(self.place.max_guest, place_dict['max_guest'])
        self.assertEqual(self.place.price_by_night,
                         place_dict['price_by_night'])
        self.assertEqual(self.place.latitude, place_dict['latitude'])
        self.assertEqual(self.place.longitude, place_dict['longitude'])
        self.assertEqual(self.place.amenity_ids, place_dict['amenity_ids'])

    def test_pycodestyle(self):
        """unittest to test pycodestyle compliance"""
        style_guide = pycodestyle.StyleGuide()
        result = style_guide.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
