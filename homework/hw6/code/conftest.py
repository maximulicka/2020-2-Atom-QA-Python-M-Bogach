import pytest
import requests
from application import flask_server
from mock_server.simple_http_server import SimpleHTTPServer
import settings


@pytest.fixture(scope='session')
def mock_http_server():
    server = SimpleHTTPServer(settings.MOCK_HOST, settings.MOCK_PORT)
    server.start()
    yield server
    server.stop()


@pytest.fixture(scope='session')
def app_flask_server():
    yield flask_server.run_app()
    requests.get('http://127.0.0.1:1050/shutdown')
