import os
import src.main
import unittest
import tempfile
import json
from itsdangerous import TimestampSigner
from src.v1.auth_controller import secret

class TestClientController(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.test_db_file = tempfile.mkstemp()
        src.main.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s' % self.test_db_file
        src.main.app.config['TESTING'] = True
        self.signer = TimestampSigner(secret)
        self.app = src.main.app.test_client()
        with src.main.app.app_context():
            src.main.init_app()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.test_db_file)

    def test_get_all_initial_clients(self):
        from itsdangerous import TimestampSigner
        response = self.app.get('/v1/client', headers={'token': self.signer.sign('tomasz')})
        json_response = json.loads(response.data)
        self.assertIsNotNone(json_response['clients'])
        self.assertEquals(len(json_response['clients']), 2)

    def test_post_new(self):
        json_payload = {
            "name": "test_post_new_client",
        }

        response = self.app.post('/v1/client',
            data = json.dumps(json_payload),
            headers = {'Content-Type': 'application/json', 'token': self.signer.sign('tomasz')})

        self.assertEquals(response.status_code, 201)

        get_all_response = self.app.get('/v1/client', headers={'token': self.signer.sign('tomasz')})
        json_response = json.loads(get_all_response.data)
        self.assertIsNotNone(json_response['clients'])
        self.assertEquals(len(json_response['clients']), 3)
        item = json_response['clients'][2]
        self.assertIsNotNone(item['feature_requests']);
        self.assertEquals(len(item['feature_requests']), 0);


if __name__ == '__main__':
    unittest.main()
