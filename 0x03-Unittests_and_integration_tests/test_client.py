#!/usr/bin/env python3
"""Test module for GithubOrgClient class"""
import unittest
from parameterized import parameterized, param
from unittest.mock import (MagicMock, PropertyMock, patch)
from client import GithubOrgClient as goc
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Test all methods implemented in GithubOrgClient"""
    @parameterized.expand(
        [("google", {'login': 'admin'}),
            ("abc", {'login': 'user'})])
    @patch('client.get_json')
    def test_org(self, org_name: str, resp: Dict,
                 mock_get_json: MagicMock) -> None:
        """Tests org function returns correct value"""
        mock_get_json.return_value = MagicMock(return_value=resp)
        gh_org_client = goc(org_name)
        self.assertEqual(gh_org_client.org(), resp)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name))

    def test_public_repos_url(self) -> None:
        """Test _public_repos_url"""
        with patch.object(goc, 'org', new_callable=PropertyMock) as mock_org:
            resp = {'repos_url': 'https://api/github/abc/users/repos'}
            mock_org.return_value = resp
            self.assertEqual(goc("abc")._public_repos_url,
                             "https://api/github/abc/users/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test public_repos"""
        test_payload = {
            'repos_url': 'https://api/github/abc/users/repos',
            'repos': [
                {
                    "id": 116722761,
                    "node_id": "MDEwOlJlcG9zaXRvcnkxMTY3MjI3NjE=",
                    "name": "abc.github.io",
                    "full_name": "abc/abc.github.io",
                    "owner": {
                      "login": "abc",
                      "id": 3063240,
                    }
                },
                {
                    "id": 440222033,
                    "node_id": "R_kgDOGj1BUQ",
                    "name": "advent-of-code-2021",
                    "full_name": "abc/advent-of-code-2021",
                    "owner": {
                      "login": "abc",
                      "id": 3063240,
                    }
                }
            ]
        }
        mock_get_json.return_value = test_payload['repos']
        with patch.object(goc, '_public_repos_url',
                          new_callable=PropertyMock) as mock_pb_url:
            mock_pb_url.return_value = test_payload['repos_url'] 
            self.assertEqual(goc("abc").public_repos(), ["abc.github.io", "advent-of-code-2021"])
            mock_pb_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        param(repo={"license": {"key": "my_license"}}, license_key="my_license", res=True),
        param(repo={"license": {"key": "other_license"}}, license_key="my_license", res=False)])
    def test_has_licence(self, repo, license_key, res):
        """Tests has_license"""
        client = goc("abc")
        has_license = client.has_license(repo, license_key)
        self.assertEqual(has_license, res)
