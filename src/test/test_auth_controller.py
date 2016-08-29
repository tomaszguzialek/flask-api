import os
import src.main
from src.models.user import User
import unittest
import tempfile
import json
import logging

class TestAuthController(unittest.TestCase):

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

    def test_login_success(self):
        login = 'test_user'
        password = 'test_pass'
        src.main.db.session.add(User(login, password))
        src.main.db.session.commit()

        json_payload = {
            "login": login,
            "password": password
        }

        response = self.app.post('/v1/auth/login',
            data = json.dumps(json_payload),
            headers = {'Content-Type': 'application/json'})
        json_response = json.loads(response.data)
        self.assertIsNotNone(json_response['user'])
        self.assertEquals((json_response['user']['login']), login)

    def test_login_incorrect_password(self):
        login = 'test_user'
        password = 'test_pass'
        src.main.db.session.add(User(login, password))
        src.main.db.session.commit()

        json_payload = {
            "login": login,
            "password": "incorrect_pass"
        }

        response = self.app.post('/v1/auth/login',
            data = json.dumps(json_payload),
            headers = {'Content-Type': 'application/json'})
        self.assertEquals(response.status_code, 403)

    def test_login_inexistent_login(self):
        login = 'test_user'
        password = 'test_pass'
        src.main.db.session.add(User(login, password))
        src.main.db.session.commit()

        json_payload = {
            "login": "inexistent_login",
            "password": password
        }

        response = self.app.post('/v1/auth/login',
            data = json.dumps(json_payload),
            headers = {'Content-Type': 'application/json'})
        self.assertEquals(response.status_code, 403)

if __name__ == '__main__':
    unittest.main()
