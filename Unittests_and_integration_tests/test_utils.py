#!/usr/bin/env python3
"""Unit Test Module
"""
import unittest
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized
from unittest.mock import Mock
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Unit Test Class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any):
        """Unit Test Method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", )),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence):
        """Test for exceptions
        """
        self.assertRaises(KeyError)

class TestGetJson(unittest.TestCase):
    """Unit Test Class for get_json
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Unit Test Method for get_json to mock and return a response
        with json
        """
        mock = Mock()
        mock.json.return_value = test_payload
        mock_get.return_value = mock

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(get_json(test_url), test_payload)

class TestMemoize(unittest.TestCase):
    """Class to test memoize
    """
    def test_memoize(self):
        """Test that when calling a_property twice, a_method is only called once"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test_class = TestClass()
            
            first_result = test_class.a_property
            second_result = test_class.a_property
            
            mock_method.assert_called_once()
            
            self.assertEqual(first_result, 42)
            self.assertEqual(second_result, 42)
