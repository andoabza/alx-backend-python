#!/usr/bin/env python3
'''test for client.py'''
from client import org
from utils import get_json
import unittest


class TestGithubOrgClient(unittest.TestCase):
    '''test for github org client'''
    def test_org(self):
        '''test org'''
        test_org = org('google')
        self.assertEqual(test_org.org, 'google')
        