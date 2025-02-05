#!/usr/bin/env python3
"""Unit test module for client.py
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Unit test class for GithubOrgClient
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_url, mock_get_json):
        """Tests GithubOrgClient.org returns the correct value
        """
        test_client = GithubOrgClient(org_url)
        test_client.org
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_url)
        )
