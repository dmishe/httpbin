#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httpbin
import unittest
import base64

from flask import json


def _string_to_base64(string):
    """Encodes string to utf-8 and then base64"""
    utf8_encoded = string.encode('utf-8')
    return base64.urlsafe_b64encode(utf8_encoded)


class HttpbinTestCase(unittest.TestCase):
    """Httpbin tests"""

    def setUp(self):
        self.app = httpbin.app.test_client()

    def test_base64(self):
        greeting = u'Здравствуй, мир!'
        b64_encoded = _string_to_base64(greeting)
        response = self.app.get('/base64/{}'.format(b64_encoded))
        content = response.data.decode('utf-8')
        self.assertEquals(greeting, content)

    def test_post(self):
        data = {'payload': u'Привет'}
        json_data = json.dumps(data)

        #returns data as string
        response = self.app.post('/post', data=json_data)
        content = json.loads(response.data.decode('utf-8'))
        self.assertEquals(json_data, content['data'])

        #returns data as JSON object
        response = self.app.post('/post?json=1', data=json_data)
        content = json.loads(response.data.decode('utf-8'))
        self.assertEquals(data, content['data'])

if __name__ == '__main__':
    unittest.main()
