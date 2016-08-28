import os
from src.main import app
import unittest
import tempfile

class TestFeatureRequestController(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['SQLALCHEMY_DATABASE_URI'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        with app.app.app_context():
            app.init()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['SQLALCHEMY_DATABASE_URI'])

    def test_get_all_empty_db(self):
        rv = self.app.get('/v1/feature_request')
        print rv
        assert b'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()
