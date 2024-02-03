#!/usr/bin/env python3
"""test for  utils.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''test case for utils'''
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a", "b"], 2),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''test access_nested_map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ['a'], None),
        ({"a": 1}, ['a', 'b'], 1)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''test nested map exception'''
        #self.assertEqual(nested_map, path, expected)
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)    


if __name__ == '__main__':
    unittest.main()
