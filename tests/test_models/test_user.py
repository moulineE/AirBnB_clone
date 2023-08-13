#!/usr/bin/python3
"""This module define a Python unittest for user.py

Unittest classes:
    TestUser

"""


import unittest
from models.user import User
import datetime
import pycodestyle


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_instance_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_attribute_types(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_str_method(self):
        expected_str = "[User] ({}) {}".format(self.user.id,
                                               self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        self.user.email = "airbnb@mail.com"
        self.user.password = "root"
        self.user.first_name = "Betty"
        self.user.last_name = "Bar"
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(self.user.id, user_dict['id'])
        self.assertEqual(self.user.created_at.isoformat(),
                         user_dict['created_at'])
        self.assertEqual(self.user.updated_at.isoformat(),
                         user_dict['updated_at'])
        self.assertEqual(self.user.email, user_dict['email'])
        self.assertEqual(self.user.password, user_dict['password'])
        self.assertEqual(self.user.first_name, user_dict['first_name'])
        self.assertEqual(self.user.last_name, user_dict['last_name'])

    def test_pycodestyle(self):
        """unittest to test pycodestyle compliance"""
        style_guide = pycodestyle.StyleGuide()
        result = style_guide.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
