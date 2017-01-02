import os
import json
from unittest import TestCase

import responses

from sageone.client import APIClient


class TestAPIClient(TestCase):

    def test_init(self):
        c = APIClient('https://x.y.z', 'b', 'c', 'd', 'e')
        self.assertEqual(c.api_key, 'b')
        self.assertEqual(c.api.__repr__(), 'https://x.y.z/api/e')

    @responses.activate
    def test_call_get(self):

        with open(
                os.path.join(os.path.dirname(__file__), 'company.json')) as fh:
            body = fh.read()

        responses.add(
            responses.GET,
            'https://x.y.z/api/e/Company/Get',
            body=body,
            status=200,
            content_type='application/json')

        c = APIClient('https://x.y.z', 'b', 'c', 'd', 'e')
        r = c('get', 'Company', 'Get')

        self.assertDictEqual(r, json.loads(body))
