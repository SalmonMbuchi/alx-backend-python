#!/usr/bin/env python3
"""Test module for GithubOrgClient class"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import (MagicMock, Mock, PropertyMock, patch)
from client import GithubOrgClient as goc
from typing import Dict
from fixtures import TEST_PAYLOAD
from requests import HTTPError


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
            self.assertEqual(goc("abc").public_repos(),
                             ["abc.github.io", "advent-of-code-2021"])
            mock_pb_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_licence(self, repo, license_key, res):
        """Tests has_license"""
        client = goc("google")
        has_license = client.has_license(repo, license_key)
        self.assertEqual(has_license, res)


@parameterized_class([{
    'org_payload': TEST_PAYLOAD[0][0],
    'repos_payload': TEST_PAYLOAD[0][1],
    'expected_repos': TEST_PAYLOAD[0][2],
    'apache2_repos': TEST_PAYLOAD[0][3],
    }])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for public_repos function"""
    @classmethod
    def setupClass(cls):
        """set up fixtures"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Test public_repos function"""
        self.assertEqual(goc("google").public_repos(), self.expected_repos)

    def test_public_repos_has_license(self) -> None:
        """Tests the public_repos function with a license"""
        self.assertEqual(goc("google").public_repos(license="apache-2.0"),
                         self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()
