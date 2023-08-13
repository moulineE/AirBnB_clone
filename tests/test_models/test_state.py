#!/usr/bin/python3
"""This module define a Python unittest for state.py

Unittest classes:
    TestState

"""

import unittest
from models.state import State
import datetime
import pycodestyle


class TestState(unittest.TestCase):

    def setUp(self):
        """creat an instance of State"""
        self.state = State()

    def test_instance_creation(self):
        """unittest the State intance creation and
        attributes setting
        """
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_attribute_types(self):
        """unittest if name is a str"""
        self.assertIsInstance(self.state.name, str)

    def test_str_method(self):
        """test BaseModel _str_method with State"""
        expected_str = "[State] ({}) {}".format(self.state.id,
                                                self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        """unittest if BaseModel to_dict_method is valid"""
        self.state.name = "The name of the state"
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(self.state.id, state_dict['id'])
        self.assertEqual(self.state.created_at.isoformat(),
                         state_dict['created_at'])
        self.assertEqual(self.state.updated_at.isoformat(),
                         state_dict['updated_at'])
        self.assertEqual(self.state.name, state_dict['name'])

    def test_pycodestyle(self):
        """unittest to test pycodestyle compliance"""
        style_guide = pycodestyle.StyleGuide()
        result = style_guide.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
