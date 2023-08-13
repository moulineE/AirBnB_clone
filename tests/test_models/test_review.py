#!/usr/bin/python3
"""This module define a Python unittest for review.py

Unittest classes:
    TestReview

"""

import unittest
from models.review import Review
import datetime
import pycodestyle


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_instance_creation(self):
        self.assertIsInstance(self.review, Review)
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_attribute_types(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_str_method(self):
        expected_str = "[Review] ({}) {}".format(self.review.id,
                                                 self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        self.review.place_id = "review place id"
        self.review.user_id = "review user id"
        self.review.text = "the reviex text"
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('__class__', review_dict)
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(self.review.id, review_dict['id'])
        self.assertEqual(self.review.created_at.isoformat(),
                         review_dict['created_at'])
        self.assertEqual(self.review.updated_at.isoformat(),
                         review_dict['updated_at'])
        self.assertEqual(self.review.place_id, review_dict['place_id'])
        self.assertEqual(self.review.user_id, review_dict['user_id'])
        self.assertEqual(self.review.text, review_dict['text'])

    def test_pycodestyle(self):
        """unittest to test pycodestyle compliance"""
        style_guide = pycodestyle.StyleGuide()
        result = style_guide.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
