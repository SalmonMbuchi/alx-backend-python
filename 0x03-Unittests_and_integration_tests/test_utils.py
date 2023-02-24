#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized, param
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json

class TestAccessNestedMap(unittest.TestCase):
    """tests access_nested_map function"""

    @parameterized.expand(
        [param({"a": 1}, ("a",), 1),
            param({"a": {"b": 2}}, ("a",), {"b": 2}),
         param({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, map, seq, expected):
        """test inputs"""
        self.assertEqual(access_nested_map(map, seq), expected)

    @parameterized.expand(
        [param({}, ("a",), KeyError),
            param({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, map, seq, expected):
        """Tests if a KeyError exception is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(map, seq)

class TestGetJson(unittest.TestCase):
    """tests get_json function"""
    @parameterized.expand(
        [param("http://example.com", {"payload": True}),
            param("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url, test_payload):
        """Return the expected payload"""
        with patch('requests.get') as mock:
            # mock = Mock(return_value=test_payload) 
            #mock.json = Mock(return_value=test_payload)
            mock.json = test_payload
            mock.get(test_url)
            mock.get.assert_called_once()
            self.assertEqual(get_json(test_url), test_payload)


if __name__ == '__main__':
    unittest.main()
