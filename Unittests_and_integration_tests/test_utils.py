#!/usr/bin/env python3
"""Unit Test Module
"""
import unittest
from utils import access_nested_map, get_json
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
    