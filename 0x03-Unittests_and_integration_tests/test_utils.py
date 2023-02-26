#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized, param
from utils import *


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
    def test_access_nested_map_exception(self, map, seq, exception):
        """Tests if a KeyError exception is raised"""
        with self.assertRaises(exception):
            access_nested_map(map, seq)


class TestGetJson(unittest.TestCase):
    """tests get_json function"""
    @parameterized.expand(
        [param("http://example.com", {"payload": True}),
            param("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url, test_payload):
        """Return the expected payload"""
        attrs = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**attrs)) as mock:
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """test memoize function"""
    def test_memoize(self):
        """parameterize and patch"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method',
                          return_value=lambda: 42)as mock:
            testclass = TestClass()
            self.assertEqual(testclass.a_property(), 42)
            self.assertEqual(testclass.a_property(), 42)
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
