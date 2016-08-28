import os
import src.main
import unittest
import tempfile
import json

class TestFeatureRequestController(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.test_db_file = tempfile.mkstemp()
        src.main.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s' % self.test_db_file
        src.main.app.config['TESTING'] = True
        self.app = src.main.app.test_client()
        with src.main.app.app_context():
            src.main.init_app()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.test_db_file)

    def test_get_all_empty_db(self):
        response = self.app.get('/v1/feature_request')
        json_response = json.loads(response.data)
        self.assertIsNotNone(json_response['feature_requests'])
        self.assertEquals(len(json_response['feature_requests']), 0)

    def test_post_new(self):
        json_payload = {
            "title": "test_post_new",
            "description": "Added from unit test"
        }

        response = self.app.post('/v1/feature_request',
            data = json.dumps(json_payload),
            headers = {'Content-Type': 'application/json'})

        self.assertEquals(response.status_code, 201)

        get_all_response = self.app.get('/v1/feature_request')
        json_response = json.loads(get_all_response.data)
        self.assertIsNotNone(json_response['feature_requests'])
        self.assertEquals(len(json_response['feature_requests']), 1)
        item = json_response['feature_requests'][0]
        del item['id']
        self.assertEquals(item, json_payload);


if __name__ == '__main__':
    unittest.main()
