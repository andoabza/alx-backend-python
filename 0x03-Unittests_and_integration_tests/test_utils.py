#!/usr/bin/env python3
"""test for  utils.
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''test for get json method'''
    def test_get_json(self):
        '''mock test for get json'''
        mock = Mock()
        mock.return_value = {'payload': True}
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json('http://example.com'),
                             {'payload': True})
        mock.json.return_value = {'payload': False}
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json('http://holberton.com'),
                             {'payload': False})


class TestMemoize(unittest.TestCase):
    '''memorize test'''
    def test_memoize(self):
        '''memorize test'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock.assert_called_once()


if __name__ == '__main__':
    '''main'''
    unittest.main()
