import os
import src.main
import unittest
import tempfile
import json
from itsdangerous import TimestampSigner
from src.v1.auth_controller import secret

class TestFeatureRequestController(unittest.TestCase):

    def setUp(self):
        src.main.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        src.main.app.config['TESTING'] = True
        self.signer = TimestampSigner(secret)
        self.app = src.main.app.test_client()
        with src.main.app.app_context():
            src.main.init_app()

    def tearDown(self):
        pass

    def test_get_all_empty_db(self):
        response = self.app.get('/v1/feature_request', headers={'token': self.signer.sign('tomasz')})
        json_response = json.loads(response.data)
        self.assertIsNotNone(json_response['feature_requests'])
        self.assertEquals(len(json_response['feature_requests']), 0)

    def test_post_new(self):
        json_payload = {
            "title": "test_post_new",
            "description": "Added from unit test",
            "client_id": 1
        }

        response = self.app.post('/v1/feature_request',
            data = json.dumps(json_payload),
            headers = {'Content-Type': 'application/json', 'token': self.signer.sign('tomasz')})

        self.assertEquals(response.status_code, 201)

        get_all_response = self.app.get('/v1/feature_request', headers={'token': self.signer.sign('tomasz')})
        json_response = json.loads(get_all_response.data)
        self.assertIsNotNone(json_response['feature_requests'])
        self.assertEquals(len(json_response['feature_requests']), 1)
        item = json_response['feature_requests'][0]
        del item['id']
        self.assertEquals(item, json_payload);


if __name__ == '__main__':
    unittest.main()
