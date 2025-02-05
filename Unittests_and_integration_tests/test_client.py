#!/usr/bin/env python3
"""Unit test module for client.py
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
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
        """TestsGithubOrgClient.org returns the correct value
        """
        test_client = GithubOrgClient(org_url)
        test_client.org
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_url)
        )

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        test_payload: dict = {"repos_url": "https://example.com/test"}
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = test_payload
            request = GithubOrgClient("test")
            result = request._public_repos_url

            self.assertEqual(result, test_payload["repos_url"])
