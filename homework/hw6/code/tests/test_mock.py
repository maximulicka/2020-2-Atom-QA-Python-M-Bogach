import pytest
import requests
from mock_server.simple_http_server import SimpleHTTPServer
import time
import json


class TestClass:

    @pytest.fixture(scope="session", autouse=True)
    def setup(self, app_flask_server, mock_http_server):
        self.app = app_flask_server
        self.mock: SimpleHTTPServer = mock_http_server
        self.mock.set_data({'max': '1', 'nick': '2'})
        time.sleep(2)

    def test_server_error(self):
        response = requests.post('http://127.0.0.1:1050/server_error')
        assert response.status_code == 500

    def test_post_auth_posit(self):
        data = {'post': 'max'}
        response = requests.post(url="http://127.0.0.1:1050/task_list",
                                 headers={"Host": "127.0.0.1",
                                          "Content-Type": "application/json",
                                          "Authorization": 'max'},
                                 data=json.dumps(data))
        assert response.status_code == 200

    def test_post_auth_neg(self):
        data = {'post': 'max'}
        response = requests.post(url="http://127.0.0.1:1050/task_list",
                                 headers={"Host": "127.0.0.1",
                                          "Content-Type": "application/json"},
                                 data=json.dumps(data))
        assert response.status_code == 403

    def test_post_auth_wrong_user(self):
        data = {'post': 'max'}
        response = requests.post(url="http://127.0.0.1:1050/task_list",
                                 headers={"Host": "127.0.0.1",
                                          "Content-Type": "application/json",
                                          "Authorization": 'julia'},
                                 data=json.dumps(data))
        assert response.status_code == 400

    def test_put_auth_posit(self):
        data = {'post': 'max'}
        response = requests.put(url="http://127.0.0.1:1050/new",
                                headers={"Host": "127.0.0.1",
                                         "Content-Type": "application/json",
                                         "Authorization": 'max'},
                                data=json.dumps(data))
        assert response.status_code == 200

    def test_put_auth_neg(self):
        data = {'post': 'max'}
        response = requests.put(url="http://127.0.0.1:1050/new",
                                headers={"Host": "127.0.0.1",
                                         "Content-Type": "application/json"},
                                data=json.dumps(data))
        assert response.status_code == 403

    def test_put_auth_wrong_user(self):
        data = {'post': 'max'}
        response = requests.put(url="http://127.0.0.1:1050/new",
                                headers={"Host": "127.0.0.1",
                                         "Content-Type": "application/json",
                                         "Authorization": 'julia'},
                                data=json.dumps(data))
        assert response.status_code == 400
