#!/usr/bin/env python3
"""test for  utils.
"""
import unittest
from parameterized import parameterized
from test_utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    '''test case for utils'''
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, a, b, expected):
        '''test for access_nested_map'''
        self.assertEqual(access_nested_map(a, b), expected)